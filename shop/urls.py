from django.contrib import admin
from django.urls import path

from shop.views import product_list, home

urlpatterns = [
    path('products/', product_list, name='products'),
    path('home/', home, name='home'),
]