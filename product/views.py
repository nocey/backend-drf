from django.shortcuts import render
from product.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from product.serializers import ProductSerializer
from rest_framework import status

# Create your views here.
# Your views accept these request
# 1- Get all product
# 2- Create product
# 3- Get single product
# 4- Update single product
# 5- Delete single product
"""
Solution 1
"""


@api_view(["GET", "POST"])
def ProductList(request):
    pass


@api_view(["GET", "POST", "PUT"])
def ProductDetails(request, pk):
    pass
