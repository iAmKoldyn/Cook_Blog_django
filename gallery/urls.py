from django.urls import path
from . import views


urlpatterns = [
    path('gallery/list', views.GalleryList.as_view(), name="gallery_list"),
    path('gallery/create', views.GalleryCreate.as_view(), name="gallery_create"),
    path('gallery/detail/<int:pk>', views.GalleryDetail.as_view(), name="gallery_retriev"),
    path('gallery/update/<int:pk>', views.GalleryUpdate.as_view(), name="gallery_update"),
    path('gallery/delete/<int:pk>', views.GalleryDelete.as_view(), name="gallery_delete"),
    path('photo/list', views.PhotoList.as_view(), name="photo_list"),
    path('photo/create', views.PhotoCreate.as_view(), name="photo_create"),
    path('photo/detail/<int:pk>', views.PhotoDetail.as_view(), name="photo_retriev"),
    path('photo/update/<int:pk>', views.PhotoUpdate.as_view(), name="photo_update"),
    path('photo/delete/<int:pk>', views.PhotoDelete.as_view(), name="photo_delete"),
]