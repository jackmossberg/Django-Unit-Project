from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views

app_name='app'
urlpatterns = [
    path('checkout/<int:pk>/', views.CheckoutView, name='checkout'),
    path('',views.home, name='home' ),
    path('search/',views.search, name='search'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login')
]