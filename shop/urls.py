from django.contrib import admin
from django.urls import path

from shop.views import details, home

urlpatterns = [
    path('home/', home, name='home'),
    path('product/<int:product_id>/', details, name='product_detail'),
]