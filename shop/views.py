from django.shortcuts import get_object_or_404

# Create your views here.
from django.shortcuts import render

from shop.models import Product


# Create your views here.

def details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'shop/detail.html', context)


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/home.html', context)
