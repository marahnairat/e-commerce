from django.db import models
from django.db.models import Model


class Product(Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_description = models.CharField(max_length=200)

    def get_price(self):
        return self.product_price



class Shops(Model):
    shop_id = models.IntegerField(primary_key=True)
    shop_name = models.CharField(max_length=250)
    shop_address = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    products = models.ManyToManyField(Product, related_name="products")

    def __str__(self):
        return self.shop_name


class Customer(Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    customer_email = models.CharField(max_length=50)
    customer_address = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name


class Order(Model):
    order_id = models.IntegerField(primary_key=True)
    order_date = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.order_date
