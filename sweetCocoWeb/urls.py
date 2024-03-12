from django.urls import path
from . import views
from .api.product import ProductListCreateView, ProductRetrieveUpdateDestroyView
from django.http import JsonResponse

app_name = 'sweetCocoWeb'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('add_product/<int:pk>/', views.add_to_cart_ajax, name='add_product'),
    path('delete_item_from_cart/<int:pk>/', views.delete_item_from_cart, name='delete_item_from_cart'),

    # API URL
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy')
]