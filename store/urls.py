from django.urls import include, path
from rest_framework import routers

from store import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSets, basename='products')
router.register(r'customers', views.CustomerViewSets, basename='customers')
router.register(r'orders', views.OrderViewSets, basename='orders')
router.register(r'reviews', views.ReviewViewSets, basename='reviews')

urlpatterns = [
    path('', include(router.urls)),
]
