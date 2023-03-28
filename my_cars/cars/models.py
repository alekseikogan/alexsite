import datetime

from django.db import models
from django.urls import reverse


# Кузов
class Body(models.Model):
    name = models.CharField(
        max_length=50,
        default='Тип кузова не выбран',
        verbose_name='Тип кузова'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Кузов'
        verbose_name_plural = 'Кузова'

    def __str__(self):
        return self.name


# Марка
class Mark(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Марка'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("show_mark", kwargs={"mark_id": self.pk})


# Машина
class Car(models.Model):
    mark = models.ForeignKey(
        Mark,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='cars',
        verbose_name='Марка',
        help_text='Кузов автомобиля'
    )
    model = models.CharField(
        max_length=100,
        default='Модель не выбрана',
        verbose_name='Модель')
    complect = models.CharField(
        max_length=70,
        blank=True,
        verbose_name='Комплектация')
    body = models.ForeignKey(
        Body,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='cars',
        verbose_name='Кузов',
        help_text='Кузов автомобиля'
    )
    description = models.TextField(null=True, blank=True)
    year = models.IntegerField(default=datetime.date.today().year)
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/',
        verbose_name='Фото',)
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления')

    class Meta:
        ordering = ('mark',)
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return (f'{self.mark} {self.model}')

    def get_absolute_url(self):
        return reverse("show_car", kwargs={"car_id": self.pk})
