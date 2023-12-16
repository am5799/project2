from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'products', ProductViewSets, basename='products')
router.register(r'customers', CustomerViewSets, basename='customers')
router.register(r'orders', OrderViewSets, basename='orders')
router.register(r'reviews', ReviewViewSets, basename='reviews')

urlpatterns = [
    path('', include(router.urls)),
]