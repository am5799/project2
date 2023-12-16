from rest_framework import serializers

from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer','firstname', 'lastname']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['quantity', 'product', 'customer', 'created_at']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['product', 'reviewer', 'rating', 'review']