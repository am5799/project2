from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'price']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'firstname', 'lastname']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'quantity', 'product', 'customer', 'created_at']


class ReviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    reviewer = CustomerSerializer()
    class Meta:
        model = Review
        fields = ['product', 'reviewer', 'rating', 'review']
