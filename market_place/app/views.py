from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .models import *
from items.models import *
from .forms import *
from django.db.models import Q
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

def signup_view(request:HttpRequest)-> HttpResponse:
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request,'app/signup.html', {'form':form})

def search(request):
    query = request.GET.get('query', '')
    category = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

        return render(request, 'app/search.html', {'items':items , 'query':query, 'category':category
        })
