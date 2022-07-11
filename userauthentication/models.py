from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="media/clent_profile_pic/%Y/%m/%d/", height_field=None, width_field=None, max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=12)
    mobile_number = models.CharField(max_length=12)

    def __str__(self):
        return self.username.username   
    
    
