from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .models import *
from items.models import *
from .forms import *
# Create your views here.
def home(request:HttpRequest)-> HttpResponse:
    Unsolditems = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    context = {
        'categories':categories,
        'items':Unsolditems,
    }
    return render(request,'app/home.html',context)

def css_test_view(request: HttpRequest)-> HttpResponse:
    return render(request, 'home.html', {'my_model_instance': Item.objects.get(pk=1)})

def category_view(request:HttpRequest)-> HttpResponse:
    context = {
        'categories':Category,
        'items':Item,
    }
    return render(request,'category.html',context)

def signin_view(request:HttpRequest)-> HttpResponse:
   
    return render(request,'signin.html')

def signup_view(request:HttpRequest)-> HttpResponse:
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request,'app/signup.html', {'form':form})

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