from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .models import *
# Create your views here.
def home_view(request:HttpRequest)-> HttpResponse:
    context = {
        'categories':Category,
        'items':Item,
    }
    return render(request,'home.html',context)

def item_view(request:HttpRequest)-> HttpResponse:
    context = {
        'categories':Category,
        'items':Item,
    }
    return render(request,'item.html',context)

def category_view(request:HttpRequest)-> HttpResponse:
    context = {
        'categories':Category,
        'items':Item,
    }
    return render(request,'category.html',context)

def signin_view(request:HttpRequest)-> HttpResponse:
   
    return render(request,'signin.html')

def signup_view(request:HttpRequest)-> HttpResponse:
    
    return render(request,'signup.html')

def cart_view(request:HttpRequest)-> HttpResponse:
    context = {
        'categories':Category,
        'items':Item,
    }
    return render(request,'cart.html',context)

def paying_view(request:HttpRequest)-> HttpResponse:
    context = {
        'categories':Category,
        'items':Item,
    }
    return render(request,'paying.html',context)