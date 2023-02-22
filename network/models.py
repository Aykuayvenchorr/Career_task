from django.db import models

from Career_task import settings


class Products(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    title = models.CharField(max_length=150, verbose_name='Название')
    model = models.CharField(max_length=50, verbose_name='Модель')
    release = models.DateField(verbose_name='Дата выхода продукта на рынок')


class Company(models.Model):
    COMPANY_TYPE_CHOICES = (
        (0, 'Завод'),
        (1, 'Региональный дистрибьютер'),
        (2, 'Розничная сеть'),
        (3, 'Магазин'),
        (4, 'Индивидуальный предприниматель'),)

    title = models.CharField(verbose_name='Название компании', max_length=250, unique=True)
    product = models.ManyToManyField(Products, verbose_name='Карточка продукта', related_name='product')
    type_of_company = models.PositiveSmallIntegerField(verbose_name='Тип контрагента', choices=COMPANY_TYPE_CHOICES, default=4)
    vendor = models.ForeignKey('self', verbose_name='Поставщик', related_name='provider', null=True, blank=True, on_delete=models.SET_NULL)
    debt = models.DecimalField(verbose_name='Задолженность перед поставщиком', max_digits=12, decimal_places=2, default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', related_name='employee', blank=True, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='Email компании контрагента', unique=True, max_length=100)
    country = models.CharField(verbose_name='Страна', max_length=100, default=None)
    city = models.CharField(max_length=100, verbose_name='Город', default=None)
    street = models.CharField(max_length=150, verbose_name='Улица', default=None)
    house = models.CharField(max_length=15, verbose_name='Дом', default=None)
    publication_date = models.DateField(verbose_name='Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Название компании'
        verbose_name_plural = 'Каталог компаний'
        ordering = ['title']
