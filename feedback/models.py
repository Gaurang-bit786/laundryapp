from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    
