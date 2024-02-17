# Model W &mdash; Wideo

This package enables easy video uploading and encoding in Wagtail.

Basic usage:
1. Add the `wideo` dependency to your `requirements.txt` or `poetry.toml` (and ensure `wagtail` and `celery` are also part of your dependencies)
2. Add `wideo` to `INSTALLED_APPS` in your Django settings
3. Optional: set `WIDEO_VIDEO_MODEL` and `WIDEO_RENDER_MODEL` to your own custom models
4. Optional: add `wideo.tasks.delete_orphan_uploaded_videos` in your `CELERY_BEAT_SCHEDULE` in order to clean up unused uploads

The `demo` folder contains an example project using Model W.

## Documentation

[✨ **Documentation is there** ✨](http://modelw-wideo.rtfd.io/)
