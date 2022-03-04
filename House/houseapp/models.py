from django.db import models

# Create your models here.

class HouseModel(models.Model):
    housename = models.CharField(max_length=250)
    housenumber = models.IntegerField(max_length=20)


