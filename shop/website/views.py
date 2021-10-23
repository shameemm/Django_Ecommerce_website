import json
from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.

def index(request):
    item = items.objects.all()
    return render(request,'index.html',{'items':item})

def cart(request):
    
    return render(request,'cart.html')

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
    return render(request,'checkout.html')