from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse
import json
# Create your views here.

def index(request):
    
    # jUST ADDed
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total': 0,'get_cart_items': 0,'shipping':False}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products':products,'cartItems':cartItems,'items':items}
    return render(request,'product_page/index.html',context) 

# def checkout(request):
#     return render(request, 'product_page/checkout.html')
@login_required(login_url='/users/login/')
def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Product.objects.filter(name__contains=searched)
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        return render(request, 'product_page/search_product.html',{'searched':searched,'products':products,'cartItems':cartItems})
        
    else:
        return render(request, 'product_page/search_product.html',{})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total': 0,'get_cart_items': 0,'shipping':False}
        cartItems = order['get_cart_items']
    
    context = {'items': items, 'order':order,'cartItems':cartItems }
    return render(request, 'product_page/cart.html',context)

@login_required(login_url='/users/login/')
def checkout(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total': 0,'get_cart_items': 0,'shipping':False}
        cartItems = order['get_cart_items']

    # receiving checkout form
    
    context = {'items': items, 'order':order,'cartItems':cartItems}
    return render(request,'product_page/checkout.html',context)

@login_required(login_url='/users/login/')
def favourite(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0,'get_cart_items': 0,'shipping':False}
        cartItems = order['get_cart_items']
        
    context = {'items': items, 'order':order,'cartItems':cartItems}
    return render(request, 'product_page/favourite.html',context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:',action)
    print('productId: ', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer,complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)

    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == 'delete':
        orderItem.quantity = 0

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)

