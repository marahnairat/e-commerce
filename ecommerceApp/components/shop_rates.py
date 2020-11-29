from .countries_currencies import get_usd_rate
from ecommerceApp.serializers import shopsSerializer


def get_shop_rate(shop, result_list):
    rate = get_usd_rate(shop)
    context = {"rate": rate}
    serializer = shopsSerializer(shop, context=context)
    result_list.append(serializer.data)

