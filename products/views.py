from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse
import json
import datetime
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

def detail(request, str):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0,'get_cart_items': 0,'shipping':False}
        cartItems = order['get_cart_items']
    
    product = Product.objects.get(name=str)
    related_product = Product.objects.filter(category=product.category).exclude(name=product.name)[:4]
    context = {'product':product,'cartItems':cartItems,'items':items,'related':related_product}
    return render(request, 'product_page/detail.html',context)

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

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        ShippingAddress.objects.create(
            customer = customer,
            order = order,
            first_name = data['shipping']['first_name'],
            last_name = data['shipping']['last_name'],
            username = data['shipping']['username'],
            email = data['shipping']['email'],
            address = data['shipping']['address'],
            city = data['shipping']['region'],
            zipcode = data['shipping']['zip'],
            payment_method = data['shipping']['payment_method'],
            name_card = data['shipping']['name_card'],
            card_number = data['shipping']['card_number'],
            expiration = data['shipping']['expiration'],
            cvv = data['shipping']['cvv'],

        )
        
    return JsonResponse('payment complete', safe=False)