from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100,verbose_name='Название')
    slug = models.SlugField(max_length=100,verbose_name='Мини-тег')
    parent = TreeForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Относится к'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    name = models.CharField(max_length=100,verbose_name='Название')
    slug = models.SlugField(max_length=100,verbose_name='Мини-тег')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE,verbose_name='Автор')
    title = models.CharField(max_length=200,verbose_name='Краткое описание')
    image = models.ImageField(upload_to='articles/',verbose_name='Изображение')
    text = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(
        Category,
        related_name="post",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория'
    )
    tags = models.ManyToManyField(Tag, related_name="post",verbose_name='Тег')
    create_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')
    slug = models.SlugField(max_length=200, unique=True,verbose_name='Мини-тег')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_single", kwargs={"slug": self.category.slug, "post_slug": self.slug})

    def get_recipes(self):
        return self.recipes.all()

    def get_comments(self):
        return self.comment.all() 

    class Meta:
        verbose_name = 'Посты' 
        verbose_name_plural = 'Посты'


class Recipe(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    serves = models.CharField(max_length=50, verbose_name='Служит')
    prep_time = models.PositiveIntegerField(default=0, verbose_name='Общее время готовки')
    cook_time = models.PositiveIntegerField(default=0,verbose_name='Время приготовленя блюда')
    ingredients = RichTextField(verbose_name='Ингредиеты')
    directions = RichTextField(verbose_name='Шаги приготовления')
    post = models.ForeignKey(
        Post,
        related_name="recipes",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Относится к посту'
    )
    class Meta:
        verbose_name = 'Рецепты'
        verbose_name_plural = 'Рецепты'


class Comment(models.Model):
    name = models.CharField(max_length=50,verbose_name='Комментатор')
    email = models.CharField(max_length=100,verbose_name='Почта')
    website = models.CharField(max_length=150, blank=True, null=True,verbose_name='Ссылка на вебсайт')
    message = models.TextField(max_length=500,verbose_name='Сообщение')
    create_at = models.DateTimeField(default=timezone.now,verbose_name='Дата публикации')
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE,verbose_name='Комментарий к посту')

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='Пользователь')
    name = models.CharField(max_length=100,verbose_name='Имя')
    email = models.CharField(max_length=100,verbose_name='Почта')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Относится к регистрации'
        verbose_name_plural = 'Относится к регистрации'
