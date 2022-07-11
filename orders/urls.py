from .views import *
from django.urls import path,include

urlpatterns = [
    path("service/",order,name='order'),
    path("place-order/<id>/",place_order,name='placeorder'),
    path("confirm-order/",confirm_order,name='confirm_order'),
    path("save-order/",save_order,name='saveorder'),
    path("order-details/",order_details,name='order_details'),
    path("card-details/<id>/",card_details,name='card_details'),
    path("check-out/",check_out,name='check_out'),
    path("payment/",payment,name='payment'),
    path("pay_premium_order/",pay_premium_order,name='pay_premium_order'),
    path("premium_order/",premium_order,name='premium_order'),
    path("premium_order_checkout/",premium_order_checkout,name='premium_order_checkout'),
]   