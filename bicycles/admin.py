from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Bicycle, MarkBicycle, Category, Country, From, Equipment, Tags, BicycleNews, Sizes, Have, Characters, CategoryProduct, MaterialRams

# admin.site.register(Bicycle)
admin.site.register(MarkBicycle)
admin.site.register(Category)
admin.site.register(Sizes)
# admin.site.register(Have)
admin.site.register(CategoryProduct)
admin.site.register(Characters)
admin.site.register(MaterialRams)
# admin.site.register(Country)
# admin.site.register(From)

@admin.register(Bicycle)

class BicycleAdmin(admin.ModelAdmin):

    list_display = ('mark','price','get_image')
    list_display_links = ('mark',)
    list_filter = ('mark', 'price', 'date',)
    search_fields = ('mark', 'price', 'date',)
    readonly_fields = ('get_full_image',)


    @admin.display(description='изображение')
    def get_image(self, bicycle):
        return mark_safe(f'<img src="{bicycle.image.url}" width="100px">')

    @admin.display(description='изображение')
    def get_full_image(self, bicycle):
        return mark_safe(f'<img src="{bicycle.image.url}" width="75%">')


@admin.register(From)


class FromAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_logos',)

    @admin.display(description='изображение')
    def image_logos(self, bicycle):
        return mark_safe(f'<img src="{bicycle.logo.url}" width="100px">')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('label', 'flag',)



    @admin.display(description='флаг')
    def flag(self, bicycle):
        return mark_safe(f'<img src="{bicycle.flag.url}" width="100px">')


@admin.register(Equipment)

class EquipmentAdmin(admin.ModelAdmin):

    list_display = ( 'description','price', 'image_equipments')
    list_display_links = ('description',)

    @admin.display(description='изображения')
    def image_equipments(self, bicycle):
        return mark_safe(f'<img src="{bicycle.image.url}" width="100px">')


@admin.register(Tags)

class TagsAdmin(admin.ModelAdmin):
    list_display = ( 'name',)
    list_display_links = ('name',)


@admin.register(BicycleNews)

class BicycleNewsAdmin(admin.ModelAdmin):
    list_display = ('description', 'date')

    @admin.display(description='изображение')
    def image_news(self, bicycle):
        return mark_safe(f'<img src="{bicycle.image.url}" width="100px">')


@admin.register(Have)
class HaveAdmin(admin.ModelAdmin):
    list_display = ('id', 'have')


# admin.site.register(News, NewsAdmin)

# Register your models here.
