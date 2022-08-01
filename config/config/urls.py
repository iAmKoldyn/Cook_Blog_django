"""cook URL Configuration
"""
from blog import views
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', include('maps.urls')),
    # path('admin/', admin.site.urls),
    path("admin/", admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("__debug__/", include(debug_toolbar.urls)),
    path("", include("contact.urls")),
    path("", include("blog.urls")),
    path("", include("gallery.urls")),
    # path('map/', views.mapbox_map, name='main'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
