from django.urls import path,include
from .views import *


urlpatterns = [
    path('premium_order_detail/',premium_order_y,name='premium_order_y'),
    path('premium_order_service/<id>/',premium_order_service,name='premium_order_service'),
    path('premium_order_confirm/',premium_order_confirm,name='premium_order_confirm'),
    path('premium_order_summary/',premium_order_summary,name='premium_order_summary'),
]