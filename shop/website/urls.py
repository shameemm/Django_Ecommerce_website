from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('update_item',views.updateItem,name='update_item'),
    path('cart',views.cart, name='cart'),
    path('single',views.single,name='single'),
    path('checkout',views.checkout,name='checkout'),
]