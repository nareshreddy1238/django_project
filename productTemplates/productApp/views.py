from django.shortcuts import render


def electronics(request):
    prod_dict = {'product1': 'Laptop', 'product2': 'Mobile', 'product3': 'Tablet'}
    return render(request, 'productApp/products.html', context=prod_dict)

def toys(request):
    prod_dict = {'product1': 'Car', 'product2': 'Doll', 'product3': 'Puzzle'}
    return render(request, 'productApp/products.html', context=prod_dict)

def shoes(request):
    prod_dict = {'product1': 'Nike', 'product2': 'Adidas', 'product3': 'Puma'}
    return render(request, 'productApp/products.html', context=prod_dict)

def index(request):
    return render(request, 'productApp/index.html')