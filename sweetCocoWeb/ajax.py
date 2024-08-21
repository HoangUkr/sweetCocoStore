from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Product, Order, OrderItem
from django.http import JsonResponse, Http404
import json

# Update total price after add to cart
def update_total(order):
    total = sum(item.subTotal() for item in OrderItem.objects.filter(order=order))
    order.total = total
    order.save()

# Add to cart AJAX function
def add_to_cart_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        recent_order, created = Order.objects.get_or_create(isSent=False)
        order_item, order_item_created = OrderItem.objects.get_or_create(order=recent_order, product=product)
        order_item.quantity += 1
        order_item.save()
        update_total(order=recent_order)
        response_data = {
            'message': 'Product added to the cart successfully',
            'errorcode': 0
        }
        return JsonResponse(response_data)
    else:
        response_data = {
            'message': 'Wrong request. Please contact admin',
            'errorcode': 1
        }
        return JsonResponse(response_data)
    
# Delete item from order
def delete_item_from_cart_ajax(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            order_id = data.get('order_id')
            order_item_id = data.get('order_item_id')
            print(f'Order ID: {order_id}. Order Item ID: {order_item_id}.')
            #Get order and order item
            order = get_object_or_404(Order, orderId=order_id)
            order_item = get_object_or_404(OrderItem, id=order_item_id, order=order)

            # Delete record
            order_item.delete()
            # Update total price in Order
            update_total(order)
            response_data = {
                'type': request.method,
                'message': 'Successfully deleted.',
                'errorcode': 0,
                'total': order.total
            }
            return JsonResponse(response_data)
        except Http404:
            response_data = {
                'type': request.method,
                'message': 'No record found.',
                'errorcode': 1,
                'total': 0
            }
            return JsonResponse(response_data)
    else:
        response_data = {
            'type': request.method,
            'message': 'Invalid request method.',
            'errorcode': 1,
            'total': 0
        }
        return JsonResponse(response_data)


# Change quantity
def change_quantity_ajax(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            order_id = data.get('order_id')
            order_item_id = data.get('order_item_id')
            # Get actiom
            action = data.get('action')

            #Get order and order item
            order = get_object_or_404(Order, orderId=order_id)
            order_item = get_object_or_404(OrderItem, id=order_item_id, order=order)

            if action == 'plus':
                order_item.quantity += 1
            else:
                if order_item.quantity > 1:
                    order_item.quantity -= 1
            order_item.save()
            update_total(order)
            response_data = {
                'type': request.method,
                'message': '',
                'errorcode': 0,
                'total': order.total
            }
            return JsonResponse(response_data)
        except Http404:
            response_data = {
                'type': request.method,
                'message': 'No record found.',
                'errorcode': 1,
                'total': 0
            }
            return JsonResponse(response_data)
    else:
        response_data = {
            'type': request.method,
            'message': 'Invalid request method.',
            'errorcode': 1,
            'total': 0
        }
        return JsonResponse(response_data)
    
# Authorisation functionality
def authorisation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Get input data
            user_name = data.get('username')
            password = data.get('password')

            # Get actiom
            action = data.get('action')

            if action.lower() == 'registration':
                pass
            else:
                user = authenticate(request, username=user_name, password=password)
                if user is not None:
                    login(request, user)
                    response_data = {
                        'type': request.method,
                        'message': 'Login successful.',
                        'authenticated': True,
                        'errorcode': 0
                    }
                    return JsonResponse(response_data)
                else:
                    response_data = {
                        'type': request.method,
                        'message': 'Wrong username or password.',
                        'authenticated': False,
                        'errorcode': 1
                    }
                    return JsonResponse(response_data)
                    
        except Http404:
            response_data = {
                'type': request.method,
                'message': 'No record found.',
                'errorcode': 1,
                'authenticated': False,
                'total': 0
            }
            return JsonResponse(response_data)
    else:
        response_data = {
            'type': request.method,
            'message': 'Invalid request method.',
            'errorcode': 1,
            'total': 0
        }
        return JsonResponse(response_data)
    
# Sign Out
def logout(request):
    response_data = {}
    try:
        print('Username: ' + request.user.username)
        logout(request)
        response_data = {
            'type': request.method,
            'message': 'Logout successful.',
            'errorcode': 0
        }
        return JsonResponse(response_data)
    except Exception:
        response_data = {
            'type': request.method,
            'message': 'Logout failed.',
            'errorcode': 100
        }
        return JsonResponse(response_data)