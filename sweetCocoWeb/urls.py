from django.urls import path
from . import views

app_name = 'sweetCocoWeb'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('shop/', views.shop, name='shop')
]