from django.db import models

# Create your models here.


class UserLogin(models.Model):
    email = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)
