from django.db import models
# from django.contrib.auth.models import AbstractUser

class Signup(models.Model):
    full_name=models.CharField(max_length=50)
    username=models.EmailField(unique=True)
    phone_number=models.IntegerField()
    password = models.CharField(max_length=10)
    location=models.CharField(max_length=50)
    
    def __str__(self):
        return self.full_name