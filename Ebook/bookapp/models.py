from django.db import models


# Create your models here.

class UserAccount(models.Model):
    username = models.CharField("Username :", max_length=25, primary_key=True)
    password = models.CharField("Password :", max_length=25)
    rights = models.CharField(max_length=25)
