from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .services.CoinDeskService.CoinDeskService import CoinDeskServiceClass

from .components.shop_rates import get_shop_rate


# class ProductsViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = productsSerializer

#
#
# class ShopsViewSet(viewsets.ModelViewSet):
#     queryset = Shops.objects.all().prefetch_related("products")
#     serializer_class = shopsSerializer
#


class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = customersSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = ordersSerializer


@api_view()
def currencies_price(request):
    coindesk_service = CoinDeskServiceClass()
    prices = coindesk_service.get_currency()
    bpi_price = prices.json()["bpi"]
    USD_price = bpi_price["USD"]
    GBP_price = bpi_price["GBP"]
    EUR_price = bpi_price["EUR"]
    result = [{"bpi": {"USD": USD_price["rate_float"], "GBP": GBP_price["rate_float"], "EUR": EUR_price["rate_float"]}}]
    return Response(result)


@api_view(['GET'])
def shops_list(request):
    shops = Shops.objects.all().prefetch_related('products')
    shop_list = list()
    for shop in shops:
        get_shop_rate(shop, shop_list)
    return Response(shop_list)


@api_view(['POST'])
def add_shop(request):
    serializer = shopsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def products_list(self):
    products = Product.objects.all()
    print("products")
    serializer = productsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_product(request):
    serializer = productsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# @api_view()
# def ameer_name(request):
#     data = {"name": "Ameer"}
#     return Response(data)


# class CurrenciesView (APIView):
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAdminUser]
#
#     def get_extra_action(self):
#         price = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
#         return Response(price)
