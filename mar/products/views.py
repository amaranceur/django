from django.shortcuts import render
from .models import Product

# Create your views here.
def product(response):
    return render(response,'products/product.html')
def products(response):
    return render(response,'products/products.html',{'pro':Product.objects.filter(name='9adour')})