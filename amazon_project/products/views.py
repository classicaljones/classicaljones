from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request,'product_page/index.html',{'products':products}) 

@login_required(login_url='/users/login/')
def checkout(request):
    return render(request, 'product_page/checkout.html')