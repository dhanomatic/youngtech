from django.db import models


# Create your models here.

class Product(models.Model):
    pname = models.CharField(max_length=25)
    qty = models.IntegerField()
    rate = models.IntegerField()

def __str__(self):
    return self.pname+ "-" + self.qty
