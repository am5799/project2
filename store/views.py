from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Product, Review, Order
from .serializers import ProductSerializer, ReviewSerializer, OrderSerializer, CustomerSerializer


class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class CustomerViewSets(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class ReviewViewSets(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
