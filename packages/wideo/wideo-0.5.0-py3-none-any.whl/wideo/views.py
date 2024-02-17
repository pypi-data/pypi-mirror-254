import json

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.transaction import atomic
from django.http import HttpRequest, HttpResponse
from django.http.multipartparser import MultiPartParser
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import NoReverseMatch, reverse
from django.utils.decorators import method_decorator
from django.utils.http import urlencode
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy, ngettext
from django.views.generic import TemplateView
from rest_framework import status
from wagtail.admin import messages
from wagtail.admin.auth import PermissionPolicyChecker
from wagtail.admin.forms.search import SearchForm
from wagtail.admin.models import popular_tags_for_model
from wagtail.admin.utils import get_valid_next_url_from_request
from wagtail.admin.views import generic
from wagtail.models import Collection
from wagtail.search.backends import get_search_backend

from . import get_render_model, get_video_model
from .forms import BaseVideoForm, VideoForm
from .models import UploadedVideo, UploadedVideoChunk
from .permissions import permission_policy

permission_checker = PermissionPolicyChecker(permission_policy)

INDEX_PAGE_SIZE = getattr(settings, "WIDEO_INDEX_PAGE_SIZE", 30)
USAGE_PAGE_SIZE = getattr(settings, "WIDEO_USAGE_PAGE_SIZE", 20)


class BaseListingView(TemplateView):
    ENTRIES_PER_PAGE_CHOICES = sorted({10, 30, 60, 100, 250, INDEX_PAGE_SIZE})
    ORDERING_OPTIONS = {
        "-created_at": _("Newest"),
        "created_at": _("Oldest"),
        "title": _("Title: (A -> Z)"),
        "-title": _("Title: (Z -> A)"),
        "file_size": _("File size: (low to high)"),
        "-file_size": _("File size: (high to low)"),
    }
    default_ordering = "-created_at"

    @method_decorator(permission_checker.require_any("add", "change", "delete"))
    def get(self, request):
        return super().get(request)

    def get_num_entries_per_page(self):
        entries_per_page = self.request.GET.get("entries_per_page", INDEX_PAGE_SIZE)
        try:
            entries_per_page = int(entries_per_page)
        except ValueError:
            entries_per_page = INDEX_PAGE_SIZE
        if entries_per_page not in self.ENTRIES_PER_PAGE_CHOICES:
            entries_per_page = INDEX_PAGE_SIZE

        return entries_per_page

    def get_valid_orderings(self):
        return self.ORDERING_OPTIONS

    def get_ordering(self):
        # TODO: remove this method when this view will be based on the
        # generic model index view from wagtail.admin.views.generic.models.IndexView
        ordering = self.request.GET.get("ordering")
        if ordering is None or ordering not in self.get_valid_orderings():
            ordering = self.default_ordering
        return ordering

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get ordering
        ordering = self.get_ordering()

        # Get videos (filtered by user permission and ordered by `ordering`)
        videos = (
            permission_policy.instances_user_has_any_permission_for(
                self.request.user, ["change", "delete"]
            )
            .order_by(ordering)
            .select_related("collection")
            # .prefetch_renditions("max-165x165")
        )

        # Filter by collection
        self.current_collection = None
        collection_id = self.request.GET.get("collection_id")
        if collection_id:
            try:
                self.current_collection = Collection.objects.get(id=collection_id)
                videos = videos.filter(collection=self.current_collection)
            except (ValueError, Collection.DoesNotExist):
                pass

        # Search
        query_string = None
        if "q" in self.request.GET:
            self.form = SearchForm(self.request.GET, placeholder=_("Search videos"))
            if self.form.is_valid():
                query_string = self.form.cleaned_data["q"]
                if query_string:
                    search_backend = get_search_backend()
                    videos = search_backend.autocomplete(query_string, videos)
        else:
            self.form = SearchForm(placeholder=_("Search videos"))

        # Filter by tag
        self.current_tag = self.request.GET.get("tag")
        if self.current_tag:
            try:
                videos = videos.filter(tags__name=self.current_tag)
            except AttributeError:
                self.current_tag = None

        entries_per_page = self.get_num_entries_per_page()
        paginator = Paginator(videos, per_page=entries_per_page)
        videos = paginator.get_page(self.request.GET.get("p"))

        next_url = reverse("wideo:index")
        request_query_string = self.request.META.get("QUERY_STRING")
        if request_query_string:
            next_url += "?" + request_query_string

        context.update(
            {
                "videos": videos,
                "query_string": query_string,
                "is_searching": bool(query_string),
                "next": next_url,
                "entries_per_page": entries_per_page,
                "ENTRIES_PER_PAGE_CHOICES": self.ENTRIES_PER_PAGE_CHOICES,
                "current_ordering": ordering,
                "ORDERING_OPTIONS": self.ORDERING_OPTIONS,
            }
        )

        return context


class IndexView(BaseListingView):
    template_name = "wideo/videos/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        collections = permission_policy.collections_user_has_any_permission_for(
            self.request.user, ["add", "change"]
        )
        if len(collections) < 2:
            collections = None

        Video = get_video_model()

        context.update(
            {
                "search_form": self.form,
                "popular_tags": popular_tags_for_model(Video),
                "current_tag": self.current_tag,
                "collections": collections,
                "current_collection": self.current_collection,
                "user_can_add": permission_policy.user_has_permission(
                    self.request.user, "add"
                ),
                "app_label": Video._meta.app_label,
                "model_name": Video._meta.model_name,
            }
        )
        return context


class ListingResultsView(BaseListingView):
    template_name = "wideo/videos/results.html"


class DeleteView(generic.DeleteView):
    model = get_video_model()
    pk_url_kwarg = "video_id"
    permission_policy = permission_policy
    permission_required = "delete"
    header_icon = "video"
    template_name = "wideo/videos/confirm_delete.html"
    usage_url_name = "wideo:video_usage"
    delete_url_name = "wideo:delete"
    index_url_name = "wideo:index"
    page_title = gettext_lazy("Delete video")

    def setup(self, request, *args, **kwargs):
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super().get_object(queryset)

    def user_has_permission(self, permission):
        return self.permission_policy.user_has_permission_for_instance(
            self.request.user, permission, self.object
        )

    @property
    def confirmation_message(self):
        return ngettext(
            "Are you sure you want to delete this video?",
            "Are you sure you want to delete these videos?",
            1,
        )

    def get_success_message(self):
        return _("Video '%(video_title)s' deleted.") % {
            "video_title": self.object.title
        }


def add(request: HttpRequest) -> HttpResponse:
    VideoModel = get_video_model()

    if request.method == "POST":
        video = VideoModel(uploaded_by_user=request.user)
        form = BaseVideoForm(request.POST, request.FILES, instance=video)

        if form.is_valid():
            # form.save()
            obj = form.save(commit=False)
            obj.save()
            form.save_m2m()

            messages.success(
                request,
                _("Video '%(video_title)s' added.") % {"video_title": video.title},
                buttons=[
                    messages.button(reverse("wideo:edit", args=(video.id,)), _("Edit"))
                ],
            )

            return redirect("wideo:index")
        else:
            messages.error(request, _("The video could not be created due to errors."))
            form = VideoForm(request.POST, request.FILES, instance=video)
    else:
        form = VideoForm()

    return TemplateResponse(
        request,
        "wideo/videos/add.html",
        {
            "form": form,
        },
    )


@permission_checker.require("change")
def edit(request, video_id):
    Video = get_video_model()
    video = get_object_or_404(Video, id=video_id)

    if not permission_policy.user_has_permission_for_instance(
        request.user, "change", video
    ):
        raise PermissionDenied

    next_url = get_valid_next_url_from_request(request)

    if request.method == "POST":
        form_data = request.POST.copy()
        form_data["upload"] = form_data.get("upload") or video.upload_id
        form = BaseVideoForm(form_data, request.FILES, instance=video)
        if form.is_valid():
            form.save()

            edit_url = reverse("wideo:edit", args=(video.id,))
            redirect_url = "wideo:index"
            if next_url:
                edit_url = f"{edit_url}?{urlencode({'next': next_url})}"
                redirect_url = next_url

            messages.success(
                request,
                _("Video '%(video_title)s' updated.") % {"video_title": video.title},
                buttons=[messages.button(edit_url, _("Edit again"))],
            )
            return redirect(redirect_url)
        else:
            messages.error(request, _("The video could not be saved due to errors."))
            form = VideoForm(request.POST, request.FILES, instance=video)
    else:
        form = VideoForm(instance=video)

    # Check if we should enable the frontend url generator
    try:
        reverse("wideo_serve", args=("foo", "1", "bar"))
        url_generator_enabled = True
    except NoReverseMatch:
        url_generator_enabled = False

    # try:
    #     filesize = video.get_file_size()
    # except SourceVideoIOError:
    #     filesize = None

    filesize = None

    return TemplateResponse(
        request,
        "wideo/videos/edit.html",
        {
            "video": video,
            "form": form,
            # This is not supported right now
            # "url_generator_enabled": url_generator_enabled,
            "filesize": filesize,
            "user_can_delete": permission_policy.user_has_permission_for_instance(
                request.user, "delete", video
            ),
            "next": next_url,
        },
    )


@permission_checker.require("delete")
def delete(request, video_id):
    video = get_object_or_404(get_video_model(), id=video_id)

    if not permission_policy.user_has_permission_for_instance(
        request.user, "delete", video
    ):
        raise PermissionDenied

    next_url = get_valid_next_url_from_request(request)

    if request.method == "POST":
        video.delete()
        messages.success(request, _("Video '{0}' deleted.").format(video.title))
        return redirect(next_url) if next_url else redirect("wideo:index")

    return TemplateResponse(
        request,
        "wideo/videos/confirm_delete.html",
        {
            "video": video,
            "next": next_url,
        },
    )


@atomic
def upload_prepare(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    upload = UploadedVideo.objects.create()
    return HttpResponse(status=status.HTTP_201_CREATED, content=upload.id)


@atomic
def upload_chunk(request: HttpRequest) -> HttpResponse:
    if request.method != "PUT":
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    data, files = MultiPartParser(
        request.META, request, request.upload_handlers
    ).parse()
    upload = get_object_or_404(UploadedVideo, id=data["upload_id"])
    UploadedVideoChunk.objects.update_or_create(
        video=upload, index=data["index"], defaults={"file": files["blob"]}
    )
    return HttpResponse(status=status.HTTP_200_OK)


def get_uploaded_video_render(
    request: HttpRequest, uploaded_video_id: int
) -> HttpResponse:
    """
    Given an UploadedVideo by its ID, return its information as if it was a
    unique Render.

    This is intended to be used in the Video add/edit templates inside Wagtail
    admin, where we expect to have an UploadedVideo instance when a video file
    is uploaded but no Video instance will be created until the form is
    submitted (therefore, no Render instance will be created yet). However, we
    still want to get the information of the video to display a preview in that
    add/edit template, so we get its information as if we were getting a unique
    Render so that we can use it with a video library.
    """
    if request.method != "GET":
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    data = {
        "type": "video",
        "title": "Video preview",
        "sources": [
            {
                "src": render.file.url,
                "type": render.mime,
                "size": render.height,
            }
            for render in get_render_model().objects.filter(
                video__upload_id=uploaded_video_id
            )
        ],
        #     poster: '/path/to/poster.jpg',
        #     previewThumbnails: {
        #         src: '/path/to/thumbnails.vtt',
        #     },
        #     tracks: [
        #         {
        #             kind: 'captions',
        #             label: 'English',
        #             srclang: 'en',
        #             src: '/path/to/captions.en.vtt',
        #             default: true,
        #         },
        #         {
        #             kind: 'captions',
        #             label: 'French',
        #             srclang: 'fr',
        #             src: '/path/to/captions.fr.vtt',
        #         },
        #     ],
    }

    return HttpResponse(status=status.HTTP_200_OK, content=json.dumps(data))
