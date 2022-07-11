from itertools import product
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField


class ClothCategory(models.Model):
    image = models.ImageField(upload_to='media/coth/category/',null=True)

    cloth_category_name = models.CharField(max_length=250)
    def __str__(self):
        return self.cloth_category_name



class ClothName(models.Model):
    cloth_category_name = models.ForeignKey("ClothCategory", on_delete=models.CASCADE)
    cloth_name = models.CharField(max_length=250)
    price = models.FloatField(null=True)
    number_of_clothes = models.CharField(max_length=250)
    def __str__(self):
        return self.cloth_name

class OrdersSummary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    cloth_name = models.ForeignKey("ClothName", on_delete=models.CASCADE)
    cloth_image = models.ImageField(upload_to="image/", null=True,blank=True)
    quantity = models.IntegerField(null=True)
    price = models.FloatField(null=True)
    ironing = models.BooleanField(default=False)
    hot_water = models.BooleanField(default=False)
    cold_water = models.BooleanField(default=False)
    washing_liquid = models.BooleanField(default=False)
    softern = models.BooleanField(default=False)
    puckup_date = models.DateField(auto_now_add=False)
    pickup_time = models.TimeField(auto_now_add=False,null=True)
    delivery = models.DateField(auto_now_add=False,null=True)
    delivery_time = models.TimeField(auto_now_add=False,null=True)
    instruction = models.CharField(max_length = 150,null=True,blank=True)
    paid = models.BooleanField(default=False)
    pick_up = models.BooleanField(default=False)
    working = models.BooleanField(default=False)
    deliver = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name


class AccountDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    card_number = models.CharField(max_length = 19)
    card_month = models.CharField(max_length = 2)
    card_year = models.CharField(max_length = 4)
    cvv = models.CharField(max_length = 150)

    def __str__(self):
        return self.user.username


class PaymentDetail(models.Model):
    image = models.ImageField(upload_to="media/payment/",null=True)
    name = models.CharField(max_length = 150)
    cloth_name = models.CharField(max_length = 150)
    price = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 150)
    mobile = models.CharField(max_length = 150)
    address = models.CharField(max_length = 250)
    quantity = models.CharField(max_length = 150)
    ironing = models.BooleanField(default=False)
    hot_water = models.BooleanField(default=False)
    cold_water = models.BooleanField(default=False)
    washing_liquid = models.BooleanField(default=False)
    softern = models.BooleanField(default=False)
    pick_up_date = models.DateField(auto_now=False, auto_now_add=False)
    delivery = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.name

