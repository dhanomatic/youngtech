from django.db import models

# Create your models here.

class ContentModel(models.Model):
    username = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=5000)



class UserModel(models.Model):
    domain = models.CharField(max_length=250)
    city =  models.CharField(max_length=250)
    country = models.CharField(max_length=250)
