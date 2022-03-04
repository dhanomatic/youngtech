from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    dob = models.DateField("date of birth", default=date.today)
    photo = models.ImageField(upload_to='images/')


class Employee(models.Model):
    name = models.CharField(max_length=20)
    job = models.CharField(max_length=30)
    salary = models.IntegerField()
    comm = models.IntegerField()
    dept = models.CharField(max_length=25)

    def __str__(self):
        return self.name +""+self.job