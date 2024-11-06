from django.shortcuts import render,get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required
from .models import Product
from django.http import JsonResponse

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request,'product_page/index.html',{'products':products}) 

@login_required(login_url='/users/login/')
def checkout(request):
    return render(request, 'product_page/checkout.html')

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Product.objects.filter(name__contains=searched)
        return render(request, 'product_page/search_product.html',{'searched':searched,'products':products})
    else:
        return render(request, 'product_page/search_product.html',{})
