from django.db import models

# Create your models here.

class Employee(models.Model):
    ename = models.CharField(max_length=50)
    job = models.CharField(max_length=50)