from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Product, Order, OrderItem
from django.http import JsonResponse
# Create your views here.

def index(request):
    return redirect(reverse('sweetCocoWeb:home'))
# Render home page
def home(request):
    return render(request, "PAGE/index.html")

# Render shop page
def shop(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'PAGE/shop.html', context=context)

# Render cart page
def cart(request):
    return render(request, 'PAGE/cart.html')

def add_to_cart_ajax(request, pk):#
    if request.method == 'POST':
        recent_order = Order.objects.filter(isSent=False).exists()
        if not recent_order :
            product = get_object_or_404(Product, pk=pk)
            print(product)
            order = Order.objects.create()
            orderItems = OrderItem.objects.create(order=order, product=product)
            orderItems.save()

            # Calculate the total price of
            total = 0
            get_orderItems = OrderItem.objects.filter(order=order)
            for item in get_orderItems:
                total += item.subTotal()
            order.total = total


        response_data = {
            'message': 'Product added to cart successfully',
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'message': 'Invalid request method.'})