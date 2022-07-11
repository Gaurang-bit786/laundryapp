from django.db import models
from django.contrib.auth.models import User


class OrdersHelp(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='help/user/',null=True)
    
    order_help = models.TextField()
    def __str__(self):
        return self.user.username


class PaymentHelp(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='help/user/',null=True)

    payment_help = models.TextField()
    def __str__(self):
        return self.user.username
    

class PackageHelp(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='help/user/',null=True)

    package_help = models.TextField()
    def __str__(self):
        return self.user.username
    