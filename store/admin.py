from django.contrib import admin
from .models import Product, Customer, Review, Order

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Review)
admin.site.register(Order)
