from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Product, Order, OrderItem
from django.http import JsonResponse, Http404
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

# Update total price after add to cart
def updateTotal(order):
    total = 0
    objectItems = OrderItem.objects.filter(order=order)
    for item in objectItems:
        total += item.subTotal()
    order.total = total
    order.save()

# Add to cart AJAX function
def add_to_cart_ajax(request, pk):
    try:
        product = get_object_or_404(Product, pk=pk)
        if request.method == 'POST':
            isRecentExist = Order.objects.filter(isSent=False).exists()
            if not isRecentExist:
                order = Order.objects.create()
                orderItems = OrderItem.objects.create(order=order, product=product)
                orderItems.save()
                updateTotal(order=order)
                response_data = {
                    'message': 'Product added to the new cart successfully',
                    'errorcode': 0
                }
            else:
                recentOrder = Order.objects.get(isSent=False)
                orderItems = OrderItem.objects.create(order=recentOrder, product=product)
                orderItems.save()
                updateTotal(order=recentOrder)
                response_data = {
                    'message': 'Product added to the existing cart successfully',
                    'errorcode': 0
                }
        else:
            response_data = {
                'message': 'Wrong request. Please contact admin',
                'errorcode': 1
            }
        return JsonResponse(response_data)
    except Http404:
        response_data = {
            'message': 'Product not found. Please contact admin.',
            'errorcode': 1
        }
        return JsonResponse(response_data)