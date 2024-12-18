from datetime import datetime

from django.db import models
from django.db.models import PROTECT
from django.utils.timezone import now


class From(models.Model):

    class Meta:
        verbose_name_plural = "производства"
        verbose_name = 'производитель'

    name = models.CharField(verbose_name='имя производства', max_length=100)
    logo = models.ImageField(verbose_name='логотип', upload_to='logos/')

    def __str__(self):
        return self.name



class Country(models.Model):

    class Meta:
        verbose_name_plural = 'страны'
        verbose_name = 'страна'

    label = models.CharField(verbose_name='имя страны', max_length=100)
    flag = models.ImageField(verbose_name='флаг страны', upload_to='images_country/')


    def __str__(self):
        return self.label



class Category(models.Model):


    class Meta:
        verbose_name_plural = "категории"
        verbose_name = 'категория'

    title = models.CharField(verbose_name='название', max_length=100)

    def __str__(self):
        return self.title


class CategoryProduct(models.Model):

    class Meta:
        verbose_name_plural = 'категории товара'
        verbose_name = 'категория товара'

    name = models.CharField(verbose_name='название категории', max_length=100)


    def __str__(self):
        return self.name

class MarkBicycle(models.Model):

    class Meta:
        verbose_name_plural = "марки велосипедов"
        verbose_name = 'марка'

    name = models.CharField(verbose_name='марка', max_length=200)


    def __str__(self):
        return self.name


class Sizes(models.Model):

    class Meta:
        verbose_name_plural = 'размеры'
        verbose_name = 'размер'

    name = models.CharField(verbose_name='название', max_length=10)

    def __str__(self):
        return self.name


class Bicycle(models.Model):

    class Meta:
        verbose_name_plural = "велосипеды"
        verbose_name = 'велосипед'

    category = models.ManyToManyField('bicycles.Category', verbose_name='категория' , related_name='bicycles', blank=True, null=True)
    mark = models.ForeignKey('bicycles.MarkBicycle', verbose_name='марка', on_delete=models.PROTECT, related_name='bicycles', blank=True, null=True)
    image = models.ImageField(verbose_name='изображение', upload_to='images_bicycle/')
    description = models.CharField(verbose_name='описание', max_length=600)
    category_product = models.ManyToManyField('bicycles.CategoryProduct', related_name='bicycles_product', blank=True, null=True)
    material = models.ForeignKey('bicycles.MaterialRams', on_delete=models.PROTECT, blank=True, null=True)
    price = models.DecimalField(verbose_name='цена', max_digits=10, decimal_places=2, default=0)
    size = models.ManyToManyField('bicycles.Sizes', verbose_name='размер', related_name='bicycles', blank=True, null=True)
    country = models.ForeignKey('bicycles.Country', on_delete=models.PROTECT, blank=True, null=True)
    edition = models.ForeignKey('bicycles.From', on_delete=PROTECT, blank=True, null=True)
    have = models.ForeignKey('bicycles.Have', on_delete=models.PROTECT, blank=True, null=True)
    characters = models.ForeignKey('bicycles.Characters', on_delete=models.PROTECT, blank=True, null=True)
    date = models.DateTimeField(verbose_name='дата публикации', default=now)



    def __str__(self):
        return self.description



class Equipment(models.Model):

    class Meta:
        verbose_name_plural = 'экипировки'
        verbose_name = 'экипровка'

    description = models.CharField(verbose_name='описание', max_length=600)
    image = models.ImageField(verbose_name='изображение', upload_to='images_equipment/')
    price = models.DecimalField(verbose_name='цена', max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        return self.description



class Tags(models.Model):

    class Meta:
        verbose_name_plural = 'тэги'
        verbose_name = 'тэг'

    name = models.CharField(verbose_name='название', max_length=100)

    def __str__(self):
        return self.name


class BicycleNews(models.Model):

    class Meta:
        verbose_name_plural = 'новости'
        verbose_name = 'новость'

    date = models.DateTimeField(verbose_name='дата публикации', auto_now_add=True)
    tag = models.ForeignKey('bicycles.Tags', on_delete=models.PROTECT, blank=True, null=True)
    description = models.CharField(verbose_name='описание', max_length=600)
    image = models.ImageField(verbose_name='изображение', upload_to='images_bicycle_news/')


    def __str__(self):
        return self.description




class MaterialRams(models.Model):

    class Meta:
        verbose_name_plural = 'материалы рам'
        verbose_name = 'материал'

    rams = models.CharField(verbose_name='материал', max_length=100)

    def __str__(self):
        return self.rams


    
class Characters(models.Model):

    class Meta:
        verbose_name_plural = 'характеристики'
        verbose_name = 'характеристика'

    color = models.CharField(verbose_name='цвет', max_length=100)
    year = models.IntegerField(verbose_name='год', blank=True, null=True)
    material = models.ForeignKey('bicycles.MaterialRams', on_delete=models.PROTECT, blank=True, null=True)
    size = models.ForeignKey('bicycles.Sizes', on_delete=models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey('bicycles.Country', on_delete=models.PROTECT, blank=True, null=True)
    edition = models.OneToOneField('bicycles.From', on_delete=PROTECT, blank=True, null=True)

    def __str__(self):
        return self.color


class Have(models.Model):

    class Meta:
        verbose_name_plural = 'наличия'
        verbose_name = 'наличие'

    have = models.CharField(verbose_name='определение', max_length=50)


    def __str__(self):
        return self.have

# Create your models here.
