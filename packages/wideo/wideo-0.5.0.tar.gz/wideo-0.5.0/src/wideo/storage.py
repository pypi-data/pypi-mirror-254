import os
from uuid import uuid4

from django.db.models import Model
from django.utils.text import slugify


def upload_to(instance: Model, filename: str) -> str:
    """
    We want to make sure to upload the file to a place that isn't going to be
    problematic.

    - In order to limit the number of files in a single directory, we use a
      random UUID in order to create a structure of directories (because most
      storage solutions have limits on the amount of files per folder).
    - The file name should be slugified (using Django's function) to make sure
      there is no problem with special characters.
    - The extension is also going to be normalized and common synonyms are
      going to be replaced by the most common one (like m4v -> mp4).

    Parameters
    ----------
    instance
        An instance
    filename
        Name of the file we're uploading
    """

    file_root, file_ext = os.path.splitext(filename)
    file_ext = file_ext.lower()

    ext_map = {".m4v": ".mp4"}

    file_ext = ext_map.get(file_ext, file_ext)
    slug = slugify(file_root)

    uuid_str = str(uuid4())
    dir_structure = os.path.join(uuid_str[:2], uuid_str[2:4], uuid_str[4:6])

    new_filename = f"{slug}{file_ext}"
    return os.path.join(__package__, dir_structure, new_filename)
