from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.

def product_list(request):
    return render(request, 'shop/detail.html')


def home(request):
    return render(request, 'shop/home.html')