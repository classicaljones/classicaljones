from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('',views.index, name='index'),
    path('cart/',views.cart, name='cart'),
    path('search/', views.search, name= 'search'),
    path('checkout/',views.checkout, name="checkout"),
    path('update_item/', views.updateItem,name='update_item'),
    path('process_order/', views.processOrder,name='process_order'),
    path('contact_us/', views.contact_us,name='contact_us'),
    path('favourite/', views.favourite,name='favourite'),
    path('contact_me/',views.contact_me,name='contact_me'),
    path('about/',views.about,name='about'),
    path('our_service/',views.our_service,name='our_service'),
    path('detail_of/<str:str>', views.detail,name='detail'),
    # path('add-to-cart/<int:product_id>/',views.add_to_cart,name='add_to_cart')
]
