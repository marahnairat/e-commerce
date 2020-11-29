from django.urls import include, path
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()

# router.register(r'hello', CurrenciesView,basename="hello")
# router.register('shops', ShopsViewSet,basename="shops")
# router.register('products', ProductsViewSet)
router.register('customers', CustomersViewSet)
router.register('orders', OrdersViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('currencies',currencies_price),
    # path('ameer',ameer_name),
    path('products/',products_list),
    path('newproduct',add_product),
    path('shops/',shops_list),
    path('newshop',add_shop),
    path('api-auth/', include('rest_framework.urls')),

]
