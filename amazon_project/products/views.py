from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
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


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0,'get_cart_items': 0}
    
    context = {'items': items, 'order':order}
    return render(request, 'product_page/cart.html',context)

def checkout(request):
    return render(request,'product_page/checkout.html')

def updateItem(request):
    return JsonResponse('Item was added', safe=False)