from django.db import models


class Photo(models.Model):
    """Класс модели галереи"""

    name = models.CharField(max_length=250,verbose_name='Название')
    image = models.ImageField(upload_to="gallery",verbose_name='Изображение')
    captions = models.TextField(blank=True,verbose_name='Подпись')
    create_date = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')
    slug = models.SlugField(max_length=255,verbose_name='Мини-тег')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"


class Gallery(models.Model):
    """Модель галереи"""

    name = models.CharField(max_length=250,verbose_name='Название')
    images = models.ManyToManyField(Photo,verbose_name='Изображение')
    captions = models.TextField(max_length=250, blank=True,verbose_name='Подпись')
    create_date = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')
    slug = models.SlugField(max_length=255,verbose_name='Мини-тег')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Галлерея"
        verbose_name_plural = "Галлерея"
