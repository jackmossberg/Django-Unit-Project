from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem
from items.models import Item
from django.contrib.auth.decorators import login_required
import stripe
from django.conf import settings
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout_cart(request):
    
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    if not cart_items:
        return redirect('/cart/')

    line_items = []
    for cart_item in cart_items:
        product = cart_item.item
        image_url = None
        if product.image:
            image_url = request.build_absolute_uri(product.image.url)

        line_items.append({
            'price_data': {
                'currency': 'usd',
                'unit_amount': int(product.price * 100), 
                'product_data': {
                    'name': product.name,
                    'images': [image_url] if image_url else [],
                },
            },
            'quantity': cart_item.quantity,
        })

    MY_DOMAIN = f"{request.scheme}://{request.get_host()}"
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        metadata={
            'user_email': request.user.email
        },
        mode='payment',
        success_url='http://127.0.0.1:8000/cart/payment-success/',
        cancel_url='http://127.0.0.1:8000/cart/',
    )

    return redirect(checkout_session.url)

@login_required
def checkout_success(request):
    CartItem.objects.filter(cart__user=request.user).delete()

    return redirect('Cart:Home')

@login_required
def add_cart(request, pk):
    added_item = get_object_or_404(Item,pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart,item=added_item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item.save()
    return redirect('app:home')

@login_required
def delete_cart(request, pk):
    cart = get_object_or_404(Cart, user=request.user)

    cart_item = get_object_or_404(CartItem, cart=cart, item_id=pk)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect("Cart:Home")

@login_required
def cart(request):
     cart, created = Cart.objects.get_or_create(user=request.user)

     items = cart.items.all()

     total = cart.total()
     total = round(total,2)

     return render(request,"cart/cart.html", {
         "cart":cart,
         'items':items,
         'total':total
     })