from .views import *
from django.urls import path

urlpatterns = [
    path('',index,name="login"),
    path('home/',home,name="home"),
    path('logout/',logout_user,name="logout"),
    path('register/',register,name="register"),
    path('user/',user_view,name="user"),
    path('user_details/',user_detail_view,name="userdetailsview"),
    path('cloth_detail/<int:id>/',clothcat,name="cloth_detail"),
    path('change_password/',change_password,name="change_password"),
]