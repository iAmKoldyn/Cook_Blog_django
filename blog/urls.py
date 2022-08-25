from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


urlpatterns = [
    path('comment/<int:pk>/', views.CreateComment.as_view(), name="create_comment"),
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name="post_single"),
    path('<slug:slug>/', views.PostListView.as_view(), name="post_list"),
    path('', views.HomeView.as_view(), name="home"),
    path('category/list', views.CategoryList.as_view(), name="category_list"),
    path('category/create', views.CategoryCreate.as_view(), name="category_create"),
    path('category/detail/<int:pk>', views.CategoryDetail.as_view(), name="category_retriev"),
    path('category/update/<int:pk>', views.CategoryUpdate.as_view(), name="category_update"),
    path('category/delete/<int:pk>', views.CategoryDelete.as_view(), name="category_delete"),
    path('tag/list', views.TagList.as_view(), name="tag_list"),
    path('tag/create', views.TagCreate.as_view(), name="tag_create"),
    path('tag/detail/<int:pk>', views.TagDetail.as_view(), name="tag_retriev"),
    path('tag/update/<int:pk>', views.TagUpdate.as_view(), name="tag_update"),
    path('tag/delete/<int:pk>', views.TagDelete.as_view(), name="tag_delete"),
    path('post/list', views.PostList.as_view(), name="post_list"),
    path('post/create', views.PostCreate.as_view(), name="post_create"),
    path('post/detail/<int:pk>', views.PostDetail.as_view(), name="post_retriev"),
    path('post/update/<int:pk>', views.PostUpdate.as_view(), name="post_update"),
    path('post/delete/<int:pk>', views.PostDelete.as_view(), name="post_delete"),
    path('recipe/list', views.RecipeList.as_view(), name="recipe_list"),
    path('recipe/create', views.RecipeCreate.as_view(), name="recipe_create"),
    path('recipe/detail/<int:pk>', views.RecipeDetail.as_view(), name="recipe_retriev"),
    path('recipe/update/<int:pk>', views.RecipeUpdate.as_view(), name="recipe_update"),
    path('recipe/delete/<int:pk>', views.RecipeDelete.as_view(), name="recipe_delete"),
    path('comment/list', views.CommentList.as_view(), name="comment_list"),
    path('comment/create', views.CommentCreate.as_view(), name="comment_create"),
    path('comment/detail/<int:pk>', views.CommentDetail.as_view(), name="comment_retriev"),
    path('comment/update/<int:pk>', views.CommentUpdate.as_view(), name="comment_update"),
    path('comment/delete/<int:pk>', views.CommentDelete.as_view(), name="comment_delete"),
]