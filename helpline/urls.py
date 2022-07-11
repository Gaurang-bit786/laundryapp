from django.urls import path,include
from helpline.views import *

urlpatterns = [
  path('order_help/',order_help,name='order_help'),  
  path('pay_help/',pay_help,name='pay_help'),  
  path('pack_help/',pack_help,name='pack_help'),  
] 
