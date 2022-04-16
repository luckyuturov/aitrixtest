from dataclasses import fields
from . import models
from rest_framework import serializers

class AdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Advert
        fields = (
            'id',
            'category',
            'subcategory',
            'title',
            'content',
            'image',
            'created_at',
            'updated_at',
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = (
            'id',
            'name'
        )

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subcategory
        fields = (
            'id',
            'name',
            'category',
        )