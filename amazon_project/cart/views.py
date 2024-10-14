from django.shortcuts import render
from .models import Product

# Create your views here.
def cart_amazon(request):
    product = Product.objects.all()
    return render(request, 'cart/index.html',{'products': product})