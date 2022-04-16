from django.shortcuts import render
from rest_framework import generics
from .models import Category, Subcategory, Advert
from .serializers import AdvertSerializer
from .serializers import CategorySerializer
from .serializers import SubcategorySerializer

class AdvertAPIView(generics.ListAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

    

class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryAPIView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
