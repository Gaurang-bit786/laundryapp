from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class PremiumClothCategory(models.Model):
    image = models.ImageField(upload_to='media/premium/category/',null=True)
    cloth_category_name = models.CharField(max_length=250)
    def __str__(self):
        return self.cloth_category_name



class PremiumClothName(models.Model):
    cloth_category_name = models.ForeignKey("PremiumClothCategory", on_delete=models.CASCADE)
    cloth_name = models.CharField(max_length=250)

    def __str__(self):
        return self.cloth_name



class PremiumOrdersSummary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    cloth_name = models.CharField(max_length=250)
    cloth_image = models.ImageField(upload_to="image/", null=True)
    quantity = models.IntegerField(null=True)
    address = models.CharField(max_length = 150,null=True)
    ironing = models.BooleanField(default=False)
    hot_water = models.BooleanField(default=False)
    cold_water = models.BooleanField(default=False)
    washing_liquid = models.BooleanField(default=False)
    softern = models.BooleanField(default=False)
    puckup_date = models.DateField(auto_now_add=False)
    delivery = models.DateField(auto_now_add=False,null=True)
    instruction = models.CharField(max_length = 150)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name


class PremiumClothService(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    premium_services_price = models.IntegerField(default=0,null=True)

    def __str__(self):
        return self.name.username

class PremiumServicePrice(models.Model):
    price = models.CharField(max_length = 150)
    def __str__(self):
        return self.price