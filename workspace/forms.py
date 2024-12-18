from importlib.metadata import requires

from django import forms

from bicycles.models import *
from django.db.models.fields import DecimalField


# from bicycles.models import MaterialRams, CategoryProduct, Country


# from bicycles.models import Bicycle


# class BicycleForm(forms.Form):
#     CREATE = 'creation'
#     UPDATE = 'updating'
#
#     def __init__(self, action=CREATE, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.action = action
#
#         if action == self.UPDATE:
#             self.fields['image'].required = False
#
#     mark = forms.ModelChoiceField(label='Марка', queryset=MarkBicycle.objects.all(), widget=forms.Select(attrs={
#         'class': 'width-form'
#     }))
#
#     image = forms.ImageField(label='Изображение велосипеда', widget=forms.FileInput(attrs={
#         'class': 'width-form width-file', 'accept': 'image/*'
#     }))
#
#     description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={
#         'class': 'textarea', 'placeholder': 'Описание', 'cols': 40, 'rows': 10
#     }))
#
#     material = forms.ModelChoiceField(
#         label='Материал рамы', queryset=MaterialRams.objects.all(), widget=forms.Select(attrs={
#             'class': 'width-form'
#         })
#     )
#
#     price = forms.FloatField(label='Цена', widget=forms.NumberInput(attrs={
#         'class': 'width-form', 'placeholder': 'Цена'
#     }))
#
#     size = forms.ModelMultipleChoiceField(
#         label='Размеры велосипедов', queryset=Sizes.objects.all(), widget=forms.CheckboxSelectMultiple()
#     )
#
#     category = forms.ModelMultipleChoiceField(label='Категория', queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple())
#
#     category_product = forms.ModelMultipleChoiceField(label='Категория продукта', queryset=CategoryProduct.objects.all(), widget=forms.CheckboxSelectMultiple())
#
#     country = forms.ModelChoiceField(label='Страна', queryset=Country.objects.all(), widget=forms.Select(attrs={
#         'class': 'width-form'
#     }))
#
#     edition = forms.ModelChoiceField(label='Страна', queryset=From.objects.all(), widget=forms.Select(attrs={
#         'class': 'width-form'
#     }))
#
#     have = forms.ModelChoiceField(label='Наличия', queryset=Have.objects.all(), widget=forms.Select(attrs={
#         'class': 'width-form'
#     }))


class BicycleForm(forms.ModelForm):
    class Meta:
        model = Bicycle
        fields = '__all__'



    widgets = {
        'category': forms.SelectMultiple(attrs={'class': 'width-form'}),
        'mark': forms.Select(attrs={'class': 'width-form'}),
        'image': forms.ClearableFileInput(attrs={'class': 'width-file'}),
        'description': forms.Textarea(attrs={'class': 'width-form', 'rows': '7'}),
        'category_product': forms.SelectMultiple(attrs={'class': 'width-form'}),
        'material': forms.Select(attrs={'class': 'width-form'}),
        'price': forms.NumberInput(attrs={'class': 'width-form'}),
        'size': forms.SelectMultiple(attrs={'class': 'width-form'}),
        'country': forms.Select(attrs={'class': 'width-form'}),
        'edition': forms.Select(attrs={'class': 'width-form'}),
        'have': forms.Select(attrs={'class': 'width-form'}),
        'character': forms.Select(attrs={'class': 'width-form'}),
        'date': forms.DateTimeInput(attrs={'type,': 'datetime-local', 'class': 'width-form'}),
    }

    labels = {
        'category': 'Категория',
        'mark': 'Марка',
        'image': 'Изображение',
        'description': 'Описание',
        'category_product': 'Категория продукта',
        'material': 'Материал',
        'price': 'Цена',
        'size': 'Размер',
        'country': 'Страна',
        'edition': 'Издание',
        'have': 'Наличие',
        'characters': 'Характеристики',
        'date': 'Дата публикации',
    }

    help_texts = {
        'price' : 'Введите цену в формате 0.00',
        'date' : 'Выбери дату публикации'
    }
