# cart/urls.py
from django.urls import path
from . import views

app_name = "Cart"

urlpatterns = [
    path('cart/checkout/', views.checkout_cart, name='checkout_cart'),
    path("", views.cart, name="Home"),
    path("add/<int:pk>/", views.add_cart, name="add"),
    path("remove/<int:pk>/", views.delete_cart, name="remove"),
    path('payment-success/', views.checkout_success, name='checkout_success'),
]
