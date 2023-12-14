from django.db import models


class Product(models.Model):
    product_id = models.IntegerField()
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)


class Customer(models.Model):
    customer_id = models.IntegerField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)


class Order(models.Model):
    order_id = models.IntegerField()
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.CharField(max_length=1000)
