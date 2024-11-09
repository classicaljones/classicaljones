from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('',views.index, name='index'),
    path('cart/',views.cart, name='cart'),
    path('search/', views.search, name= 'search'),
    path('checkout/',views.checkout, name="checkout"),
    path('update_item/', views.updateItem,name='update_item')
    # path('add-to-cart/<int:product_id>/',views.add_to_cart,name='add_to_cart')
]
