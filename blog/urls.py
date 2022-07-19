from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


urlpatterns = [
    path('comment/<int:pk>/', views.CreateComment.as_view(), name="create_comment"),
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name="post_single"),
    path('<slug:slug>/', views.PostListView.as_view(), name="post_list"),
    # path('', cache_page(60 * 15)(views.HomeView.as_view()), name="home"),
    path('', views.HomeView.as_view(), name="home"),

    # path("loggedin_contact/", views.loggedin_contact, name="loggedin_contact"),
    path("register/", views.register, name="register"),
    path("change_password/", views.change_password, name="change_password"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
]
