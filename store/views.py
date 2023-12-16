from rest_framework import viewsets

from store.models import Product, Customer, Review, Order
from store.serializers import ProductSerializer, CustomerSerializer, ReviewSerializer, OrderSerializer


class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomerViewSets(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ReviewViewSets(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
