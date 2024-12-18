from pprint import pprint

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from workspace.forms import BicycleForm

from bicycles.models import Category, MarkBicycle, Bicycle, CategoryProduct, From, MaterialRams, Sizes, Country, Have


def workspace(request):
    bicycles = Bicycle.objects.all()
    categories = Category.objects.all()
    category = CategoryProduct.objects.all()
    mark = MarkBicycle.objects.all()
    name_from = From.objects.all()
    material = MaterialRams.objects.all()

    page_size = int(request.GET.get('limit', 6))
    page = int(request.GET.get('page', 1))

    paginator = Paginator(bicycles, page_size)
    bicycles = paginator.get_page(page)
    return render(request, 'workspace/index.html', {
        'bicycles': bicycles,

        'categories': categories,
        'category': category,
        'mark': mark,
        'name_from': name_from,
        'material': material,
    })










#

# create-2-form
# def create_bicycles(request):
#
#     form = BicycleForm()
#
#     if request.method == "POST":
#         form = BicycleForm(data=request.POST, files=request.FILES)
#
#         if form.is_valid():
#             pprint(form.cleaned_data)
#
#             image = form.cleaned_data.pop('image')
#             size = form.cleaned_data.pop('size')
#             category = form.cleaned_data.pop('category')
#             category_product = form.cleaned_data.pop('category_product')
#
#             bicycle = Bicycle.objects.create(**form.cleaned_data)
#             bicycle.image.save(image.name, image)
#
#
#             bicycle.category.add(*category)
#             bicycle.category_product.add(*category_product)
#             bicycle.size.add(*size)
#
#
#             bicycle.save()
#
#             return redirect('/workspace/')
#
#         print(form.errors)
#
#     return render(request, 'workspace/create_bicycles.html', {'form': form})









# update-2-form
# def update_bicycles(request, id):
#     bicycle = get_object_or_404(Bicycle, id=id)
#     form = BicycleForm(action=BicycleForm.UPDATE,initial={
#         'mark': bicycle.mark,
#         'description': bicycle.description,
#         'material': bicycle.material,
#         'price': bicycle.price,
#         'size': bicycle.size.all(),
#         'category': bicycle.category.all(),
#         'category_product': bicycle.category_product.all(),
#         'country': bicycle.country,
#         'edition': bicycle.edition,
#         'have': bicycle.have,
#     })
#
#     if request.method == "POST":
#         form = BicycleForm(data=request.POST, files=request.FILES, action=BicycleForm.UPDATE)
#         if form.is_valid():
#             image = form.cleaned_data.pop('image')
#             size = form.cleaned_data.pop('size')
#             category = form.cleaned_data.pop('category')
#             category_product = form.cleaned_data.pop('category_product')
#
#             bicycle.size.clear()
#             bicycle.size.add(*size)
#             bicycle.category.clear()
#             bicycle.category.add(*category)
#             bicycle.category_product.clear()
#             bicycle.category_product.add(*category_product)
#
#             if image is not None:
#                 bicycle.image.save(image.name, image)
#
#
#             bicycle.save()
#
#             Bicycle.objects.filter(id=id).update(**form.cleaned_data)
#

            # old 2-method form
            # bicycle.mark = form.cleaned_data.get('mark')
            # bicycle.description = form.cleaned_data.get('description')
            # bicycle.material = form.cleaned_data.get('material')
            # bicycle.price = form.cleaned_data.get('price')
            # bicycle.country = form.cleaned_data.get('country')
            # bicycle.edition = form.cleaned_data.get('edition')
            # bicycle.have = form.cleaned_data.get('have')
            #
            # bicycle.size.set(form.cleaned_data.get('size'))
            # bicycle.category.set(form.cleaned_data.get('category'))
            # bicycle.category_product.set(form.cleaned_data.get('category_product'))

    #         return redirect('/workspace/')
    #
    # return render(request, 'workspace/update_bicycles.html', {'form': form, 'bicycle': bicycle, 'id': id})





# create-1-method
# def create_bicycles(request):
#     bicycles = None
#
#     if request.method == "POST":
#         mark_instance = MarkBicycle.objects.get(id=int(request.POST.get('mark')))
#         material_instance = MaterialRams.objects.get(id=int(request.POST.get('material')))
#         country = Country.objects.get(id=int(request.POST.get('country')))
#
#         bicycles = Bicycle.objects.create(
#             mark=mark_instance,
#             description=request.POST['description'],
#             price=request.POST['price'],
#             material=material_instance,
#             have=Have.objects.get(id=int(request.POST.get('have'))),
#             country=country,
#         )
#
#         # have_id = request.POST.get('have')
#         # have = Have.objects.filter(id=have_id)
#         # bicycles.have.add(have)
#         # bicycles.save()
#
#         category_ids = list(request.POST.getlist('category'))
#         category_product_ids = list(request.POST.getlist('category_product'))
#         all_category_ids = category_ids + category_product_ids
#
#         categories = Category.objects.filter(id__in=all_category_ids)
#         bicycles.category.add(*categories)
#
#         image = request.FILES.get('image')
#         if image:
#             bicycles.image.save(image.name, image)
#
#         flag = request.FILES.get('flag')
#         if flag:
#             bicycles.image.save(flag.name, flag)
#
#         bicycles.save()
#
#         return redirect('/workspace/')
#
#         # countries = Country.objects.all()
#     title = 'Catalogue'
#     haves = Have.objects.all()
#     categories = Category.objects.all()
#     marks = MarkBicycle.objects.all()
#     sizes = Sizes.objects.all()
#     category_product = CategoryProduct.objects.all()
#     countries = Country.objects.all()
#     editions = From.objects.all()
#     materials = MaterialRams.objects.all()
#
#     return render(request, 'workspace/create_bicycles.html', {
#         'categories': categories,
#         'marks': marks,
#         'sizes': sizes,
#         'category_product': category_product,
#         'countries': countries,
#         'editions': editions,
#         'materials': materials,
#         'haves': haves,
#         'title': title,
#     })






# update-1-method
# def update_bicycles(request, id):
#     bicycles = get_object_or_404(Bicycle, id=id)
#
#     if request.method == "POST":
#         bicycles.description = request.POST.get('description')
#         bicycles.price = request.POST.get('price').replace(',', '.')
#
#
#         size_id = list(map(int, request.POST.getlist('sizes')))
#         sizes = Sizes.objects.filter(id__in=size_id)
#         bicycles.size.clear()
#         bicycles.size.add(*sizes)
#
#         mark_id = int(request.POST.get('mark'))
#         mark = MarkBicycle.objects.get(id=mark_id)
#         bicycles.mark = mark
#         bicycles.save()
#
#         country_id = int(request.POST.get('country'))
#         country = Country.objects.get(id=country_id)
#         bicycles.country = country
#         bicycles.save()
#
#         edition_id = int(request.POST.get('edition'))
#         edition = From.objects.get(id=edition_id)
#         bicycles.edition = edition
#         bicycles.save()
#
#
#         category_id = list(map(int, request.POST.getlist('category')))
#         category = Category.objects.filter(id__in=category_id)
#         bicycles.category.clear()
#         bicycles.category.add(*category)
#
#         category_product_id = list(map(int, request.POST.getlist('category_product')))
#         category_product = CategoryProduct.objects.filter(id__in=category_product_id)
#         bicycles.category_product.clear()
#         bicycles.category_product.add(*category_product)
#
#         print(request.POST.getlist('category'))
#
#         image = request.FILES.get('image')
#         if image is not None:
#             bicycles.image.save(image.name, image)
#
#         bicycles.save()
#
#         return redirect('/workspace/')
#
#     haves = Have.objects.all()
#     categories = Category.objects.all()
#     marks = MarkBicycle.objects.all()
#     sizes = Sizes.objects.all()
#     category_product = CategoryProduct.objects.all()
#     countries = Country.objects.all()
#     editions = From.objects.all()
#     materials = MaterialRams.objects.all()
#
#
#     return render(request, 'workspace/update_bicycles.html', {
#         'bicycles': bicycles,
#         'categories': categories,
#         'marks': marks,
#         'sizes': sizes,
#         'category_product': category_product,
#         'countries': countries,
#         'editions': editions,
#         'materials': materials,
#         'haves': haves,
#     })


def delete_bicycle(request, id):
    bicycle = get_object_or_404(Bicycle, id=id)
    bicycle.delete()
    return redirect('/workspace/')


# 3-method
#
#
#
#
def create_bicycles (request):
    if request.method == 'POST':
        form = BicycleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/workspace/')
    else:
            form = BicycleForm()

    return render(request, 'workspace/create_bicycles.html', {'form': form})

def update_bicycles (request, id):
    bicycle = get_object_or_404(Bicycle, id=id)
    if request.method == 'POST':
        form = BicycleForm(request.POST, request.FILES, instance=bicycle)
        if form.is_valid():
            form.save()
            return redirect('/workspace/')
    else:
        form = BicycleForm(instance=bicycle)
    return render(request, 'workspace/update_bicycles.html', {'form': form, 'id': id})
#



# Create your views here.

