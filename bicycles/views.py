from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from bicycles.models import (Bicycle, MarkBicycle,
                             Category, From, Equipment,
                             BicycleNews, Characters, Sizes,
                             CategoryProduct, MaterialRams, Have)


def main(request, id=1):
    cat1 = get_object_or_404(Category, id=1)
    bike = Bicycle.objects.filter(category=cat1)
    cat2 = get_object_or_404(Category, id=2)
    bike2 = Bicycle.objects.filter(category=cat2)

    cats = get_object_or_404(Category, id=id)

    title = 'Bicycles.kg'
    categories = Category.objects.all()
    froms = From.objects.all()
    bicycles = Bicycle.objects.all()
    equipments = Equipment.objects.all()
    bicyclenews = BicycleNews.objects.all()
    # news = News.objects.filter(is_published=True)



    return render(request, 'index.html',
    {'categories': categories,
            'froms': froms,
            'bicycles': bicycles,
            'equipments': equipments,
            'bicyclenews': bicyclenews,
            'title': title,
            'bike': bike,
            'bike2': bike2,
            'cats': cats,
     })


def equipments(request):
    # bicycles = Bicycle.objects.all()
    have = Have.objects.get(id=1)
    have_2 = Have.objects.get(id=3)
    # print("Количество велосипедов:", bicycles.count())  # Для отладки
    categories = Category.objects.all()
    category = CategoryProduct.objects.all()
    mark = MarkBicycle.objects.all()
    name_from = From.objects.all()
    material = MaterialRams.objects.all()
    equipments = Equipment.objects.all()

    return render(request, 'equipments.html',
                  # {'bicycles': bicycles,
                  {
                   'categories': categories,
                   'mark': mark,
                   'category': category,
                   'name_from': name_from,
                   'material': material,
                   'have': have,
                   'have_2': have_2,
                   'equipments': equipments,
                   })



def catalogue(request):
    bicycles = Bicycle.objects.all()
    have = Have.objects.get(id=1)
    have_2 = Have.objects.get(id=3)
    # print("Количество велосипедов:", bicycles.count())  # Для отладки
    categories = Category.objects.all()
    # product =
    category = CategoryProduct.objects.all()
    mark = MarkBicycle.objects.all()
    name_from = From.objects.all()
    material = MaterialRams.objects.all()
    equipments = Equipment.objects.all()


    search = request.GET.get('search')
    print(search)

    if search is not None:
        bicycles = bicycles.filter(mark__name__icontains=search)



    page_size = int(request.GET.get('limit', 6))
    page = int(request.GET.get('page', 1))
    bicycles = Bicycle.objects.all().order_by('id')

    paginator = Paginator(bicycles, page_size)
    bicycles = paginator.get_page(page)

    print(bicycles.has_previous(), bicycles.has_next())

    return render(request, 'catalogue.html',
    {'bicycles': bicycles,
            'categories': categories,
            'mark': mark,
            'category': category,
            'name_from': name_from,
            'material': material,
            'have': have,
            'have_2': have_2,
            'equipments': equipments,
    })
    # froms = From.objects.all()
    # return render(request, 'catalogue.html', {'bicycles': bicycles, 'categories':categories, 'froms':froms})




def detail_bicycles(request, id):
    bicycles = Bicycle.objects.get(id=id)
    # news.views += 1
    # news.save()
    sizes = Sizes.objects.all()
    characters = Characters.objects.all()
    categories = Category.objects.all()
    return render(request, 'detail_bicycles.html',
                  {'bicycles': bicycles, 'categories': categories, 'characters': characters, 'sizes': sizes})

# Create your views here.
