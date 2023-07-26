from django.shortcuts import render, redirect
from mainApp.models import Product, Category


# Create your views here.
def all_products_page(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'main.html', context=context)


def update_product_page(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        count_on_stock = request.POST.get('count_on_stock')
        category = request.POST.get('category')

        category_data = Category.objects.get(name=category)

        Product.objects.filter(pk=pk).update(
            name=name,
            price=price,
            count_on_stock=count_on_stock,
            category=category_data
        )

    products = Product.objects.get(pk=pk)
    context = {'products': products}
    return render(request, 'updatePage.html', context=context)


def delete_product(request, pk):
    Product.objects.get(pk=pk).delete()
    return redirect('http://127.0.0.1:8000/')
