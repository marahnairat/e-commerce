from django.db.models import Prefetch
from rest_framework import serializers
from .models import *


class productsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_id', 'product_name', 'product_price', 'product_description')


class shopProductsSerializer(serializers.ModelSerializer):
    local_price = serializers.SerializerMethodField()

    def get_local_price(self, obj):
        rate = self.context['rate']
        local_price = rate * obj.product_price
        return local_price

    class Meta:
        model = Product
        fields = ('product_id', 'product_name', 'product_price', 'product_description', 'local_price')


class shopsSerializer(serializers.ModelSerializer):
    products = shopProductsSerializer(many=True)

    class Meta:
        model = Shops
        fields = '__all__'


class customersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ordersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
