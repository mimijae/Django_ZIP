from django.shortcuts import render
from rest_framework.views import ModelViewSet
from .serializer import ProductSerializer
from .models import Product
# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer