from django.urls import path,include
from .views  import data, PaymentList,ChartData
urlpatterns = [
    path('data/',data,name='data'),
    path('cd/',ChartData.as_view(),name='cd'),
    path('api/order/',PaymentList.as_view())
]