from django.db import models

# Create your models here.

class Employee(models.Model):
    ename = models.CharField(max_length=50)
    job = models.CharField(max_length=50)

class Student(models.Model):
    name = models.CharField(max_length=25)
    place = models.CharField(max_length=25)

class Useraccount(models.Model):
    uname = models.CharField(max_length=30)
    pword = models.CharField(max_length=30)
    right = models.CharField(max_length=30)