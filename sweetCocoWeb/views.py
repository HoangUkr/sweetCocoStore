from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Product, Order, OrderItem

# Create your views here.

def index(request):
    return redirect(reverse('sweetCocoWeb:home'))
# Render home page
def home(request):
    context = {
        'user': request.user
    }
    print('Username: ' +str(request.user.username))
    print('Is authenticated: ' +str(request.user.is_authenticated))
    return render(request, "PAGE/index.html", context)

# Render shop page
def shop(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'PAGE/shop.html', context=context)

# Render cart page
def cart(request):
    order = Order.objects.filter(isSent=False).first()
    if order:
        order_items = OrderItem.objects.filter(order=order)
    else:
        order_items = OrderItem.objects.none()
    context = {
        'order': order,
        'orderItems': order_items
    }
    return render(request, 'PAGE/cart.html', context=context)