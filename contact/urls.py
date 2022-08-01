from django.urls import path
from . import views


urlpatterns = [
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('feedback/', views.CreateContact.as_view(), name="feedback"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('about/list', views.AboutList.as_view(), name="about_list"),
    path('about/create', views.AboutCreate.as_view(), name="about_create"),
    path('about/detail/<int:pk>', views.AboutDetail.as_view(), name="about_retriev"),
    path('about/update/<int:pk>', views.AboutUpdate.as_view(), name="about_update"),
    path('about/delete/<int:pk>', views.AboutDelete.as_view(), name="about_delete"),
    path('contactLink/list', views.ContactLinkList.as_view(), name="contactLink_list"),
    path('contactLink/create', views.ContactLinkCreate.as_view(), name="contactLink_create"),
    path('contactLink/detail/<int:pk>', views.ContactLinkDetail.as_view(), name="contactLink_retriev"),
    path('contactLink/update/<int:pk>', views.ContactLinkUpdate.as_view(), name="contactLink_update"),
    path('contactLink/delete/<int:pk>', views.ContactLinkDelete.as_view(), name="contactLink_delete"),
    path('contactModel/list', views.ContactModelList.as_view(), name="contactModel_list"),
    path('contactModel/create', views.ContactModelCreate.as_view(), name="contactModel_create"),
    path('contactModel/detail/<int:pk>', views.ContactModelDetail.as_view(), name="contactModel_retriev"),
    path('contactModel/update/<int:pk>', views.ContactModelUpdate.as_view(), name="contactModel_update"),
    path('contactModel/delete/<int:pk>', views.ContactModelDelete.as_view(), name="contactModel_delete"),
    path('social/list', views.SocialList.as_view(), name="social_list"),
    path('social/create', views.SocialCreate.as_view(), name="social_create"),
    path('social/detail/<int:pk>', views.SocialDetail.as_view(), name="social_retriev"),
    path('social/update/<int:pk>', views.SocialUpdate.as_view(), name="social_update"),
    path('social/delete/<int:pk>', views.SocialDelete.as_view(), name="social_delete"),
]
