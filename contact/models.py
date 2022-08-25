from ckeditor.fields import RichTextField
from django.db import models


class ContactModel(models.Model):
    """ Класс модели обратной связи"""
    name = models.CharField(max_length=50,verbose_name='Никнейм')
    email = models.EmailField(verbose_name='Почта')
    website = models.URLField(blank=True, null=True,verbose_name='Вебсайт')
    message = models.TextField(max_length=5000,verbose_name='Сообщение')
    create_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата регистрации')

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'Контакты пользователей'
        verbose_name_plural = 'Контакты пользователей'


class ContactLink(models.Model):
    """ Класс модели контактов """
    icon = models.FileField(upload_to="icons/",verbose_name='Иконка')
    name = models.CharField(max_length=200,verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локация'


class About(models.Model):
    """ Класс модели страницы о нас """
    name = models.CharField(max_length=50, default='',verbose_name='Создатель')
    text = RichTextField(verbose_name='Основной текст')
    mini_text = RichTextField(verbose_name='краткое описание')

    def get_first_image(self):
        item = self.about_images.first()
        return item.image.url

    def get_images(self):
        return self.about_images.order_by('id')[1:]
   
    class Meta:
        verbose_name = 'Страница About'
        verbose_name_plural = 'Страница About'


class ImageAbout(models.Model):
    """ Класс модели изображений страницы о нас """
    image = models.ImageField(upload_to="about/",verbose_name='Изображение')
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name="about_images",verbose_name='Страница')
    alt = models.CharField(max_length=100, verbose_name='Мини-тег')


class Social(models.Model):
    """ Класс модели соцю сетей страницы о нас """
    icon = models.FileField(upload_to="icons/", verbose_name='Иконка')
    name = models.CharField(max_length=200,verbose_name='Название ресурса')
    link = models.URLField(verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Социальные ссылки'
        verbose_name_plural = 'Социальные ссылки'


class Order(models.Model):
    """ Класс модели регистрации """
    STATUS = ()
