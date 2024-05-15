from django.urls import path
from .views import *
from .ajax import *
from .api.product import ProductListCreateView, ProductRetrieveUpdateDestroyView

app_name = 'sweetCocoWeb'
urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path('login/', login, name='login'),
    path('add_product/', add_to_cart_ajax, name='add_product'),
    path('delete_item_from_cart/', delete_item_from_cart_ajax, name='delete_item_from_cart'),
    path('change_quantity/', change_quantity_ajax, name='change_quantity'),

    # Login and registration
    path('authorisation/', authorisation, name='authorisation'),

    # API URL
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy')
]