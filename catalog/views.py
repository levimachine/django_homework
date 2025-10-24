from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()
    context = {
        'objects_list': product_list
    }
    return render(request, 'catalog/home.html', context)


def product_details(request, product_id):
    context = {
        'product': get_object_or_404(Product, id=product_id),
    }
    return render(request, 'catalog/product_details.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"""Пришли данные:
Имя: {name}
Телефон: {phone}
Сообщение: {message}""")
    return render(request, 'catalog/contacts.html')


def products(request):
    product_list = Product.objects.all()
    context = {
        'objects_list': product_list
    }
    return render(request, 'catalog/products.html', context)
