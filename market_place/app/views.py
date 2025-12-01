from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .models import *
from items.models import *
from .forms import *
from django.db.models import Q
import stripe
# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY
@login_required
def CheckoutView(request, pk):
    product = Item.objects.get(id=pk)
    image_url = None
    if product.image:
        image_url = request.build_absolute_uri(product.image.url)
    print (image_url)
    MY_DOMAIN = f"{request.scheme}://{request.get_host()}"
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency':'usd',
                'unit_amount':int(product.price * 100),
                'product_data': {
                    "name":product.name,
                    'images':[image_url] if image_url else [],
                },
            },
            'quantity':1,
        },
    ],
    metadata = {
        'product_id':pk,
        'user_email':request.user.email
    },
    mode='payment',
    success_url=MY_DOMAIN + f'/payment-success/{pk}',
    cancel_url=MY_DOMAIN + f'/pricing/{pk}',
    )
    return redirect(checkout_session.url)

def Log_out(request):
    logout(request)
    return redirect('/app/login/')

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
@login_required
def cart(request):
    items = Item.objects.filter()
    return render(request,'cart.html', {'items':items
    })
  