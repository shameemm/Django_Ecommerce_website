import json
from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        
    else:
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']
    products = items.objects.all()
    context = {'products':products}
    return render(request,'index.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items =[]
        order = {'get_cart_total':0,'get_cart_items':0}
    context = {'items':items,'order':order}
    return render(request,'cart.html',context)

def single(request):
    item = items(items.id==1)
    return render(request,'single.html',{'item':item})

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('product',productId)
    print('action',action)

    customer = request.user.customer
    product = items.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)

    if action=='add':
        orderItem.quantity = (orderItem.quantity +1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse('Item was added',safe=False)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
    context = {'items':items,'order':order}
    return render(request,'checkout.html',context)