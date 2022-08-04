"""cook URL Configuration
"""
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path("admin/", admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("__debug__/", include(debug_toolbar.urls)),
    path("", include("contact.urls")),
    path("", include("blog.urls")),
    path("", include("gallery.urls")),
    path("api/v1/dr-auth/", include("rest_framework.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
