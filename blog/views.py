from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from .models import *
from .forms import CommentForm
from .serializers import *


class HomeView(ListView):
    model = Post
    paginate_by = 9
    template_name = "blog/home.html"


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()


def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":   
            username = request.POST['username']
            full_name=request.POST['full_name']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            phone_number = request.POST['phone_number']
            email = request.POST['email']

            if password1 != password2:
                alert = True
                return render(request, "register.html", {'alert':alert})
            
            user = User.objects.create_user(username=username, password=password1, email=email)
            customers = Customer.objects.create(user=user, name=full_name, phone_number=phone_number, email=email)
            user.save()
            customers.save()
            return render(request, "login.html")
    return render(request, "register.html")

def Login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                alert = True
                return render(request, "login.html", {"alert":alert})
    return render(request, "login.html")

def Logout(request):
    logout(request)
    alert = True
    return render(request, "index.html", {'alert':alert})


# rest


class CategoryList(ListAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreate(CreateAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryDetail(RetrieveAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdate(UpdateAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryDelete(DestroyAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class TagList(ListAPIView):
    model = Tag
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagCreate(CreateAPIView):
    model = Tag
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]


class TagDetail(RetrieveAPIView):
    model = Tag
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagUpdate(UpdateAPIView):
    model = Tag
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]


class TagDelete(DestroyAPIView):
    model = Tag
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostList(ListAPIView):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreate(CreateAPIView):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostDetail(RetrieveAPIView):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdate(UpdateAPIView):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostDelete(DestroyAPIView):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecipeList(ListAPIView):
    model = Recipe
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeCreate(CreateAPIView):
    model = Recipe
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]


class RecipeDetail(RetrieveAPIView):
    model = Recipe
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeUpdate(UpdateAPIView):
    model = Recipe
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecipeDelete(DestroyAPIView):
    model = Recipe
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentList(ListAPIView):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentCreate(CreateAPIView):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentDetail(RetrieveAPIView):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdate(UpdateAPIView):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentDelete(DestroyAPIView):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]