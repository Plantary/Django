from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def storemain(request):
    products = Product.objects
    return render(request, 'store.html', {'products':products})

def storemanager(request):
    products = Product.objects
    return render(request, 'storemanager.html', {'products':products})    

def registerproduct(request):
    return render(request, 'registerproduct.html')

def productdetail(request, product_id):
    product_detail = get_object_or_404(Product, pk=product_id)
    return render(request, 'productdetail.html', {'product':product_detail})