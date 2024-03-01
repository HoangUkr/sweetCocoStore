from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

def index(request):
    return redirect(reverse('sweetCocoWeb:home'))
# Render home page
def home(request):
    return render(request, "PAGE/index.html")

# Render shop page
def shop(request):
    return render(request, 'PAGE/shop.html')

# Render cart page
def cart(request):
    return render(request, 'PAGE/cart.html')