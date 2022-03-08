from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

# utype = (
#     ("New Department", "New Department"),
#     ("user","user"),
# )

class UserReg(models.Model):
    uid = models.IntegerField(primary_key=True)
    username = models.CharField("Username : ", max_length=30, unique=True)
    password = models.CharField("Password : ", max_length=15)
    email = models.EmailField("Email :")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$',
                                 message="phone number must be entered in the format: '+91'. Up to 12 digital allowed.")
    phone_number = models.CharField("Phone number :", validators=[phone_regex], max_length=17, blank=False)
    panchayath = models.CharField("Enter your panchayath : ", max_length=30)
    district = models.CharField("Enter your district : ", max_length=30)
    state = models.CharField("Enter your state : ", max_length=30)
    country = models.CharField("Enter your country " , max_length=30)
    fname = models.CharField("First Name : ", max_length=30)
    lname = models.CharField("Last Name : ", max_length=30)
    house_name = models.CharField("House Name : ", max_length=50)
    house_number = models.IntegerField("House Number : ")
    gender = models.CharField("Gender : ", max_length=20)
    dob = models.DateField("Date of Birth : ")
    photo = models.ImageField(upload_to='images/')

class DeptReg(models.Model):
    did = models.IntegerField(primary_key=True)
    username = models.CharField("Username : ", max_length=30, unique=True)
    password = models.CharField("Password : ", max_length=15)
    email = models.EmailField("Email :")
    department = models.CharField("Department : ", max_length=30)
    panchayath = models.CharField("Enter your panchayath : ", max_length=30)
    district = models.CharField("Enter your district : ", max_length=30)
    state = models.CharField("Enter your state : ", max_length=30)
    country = models.CharField("Enter your country ", max_length=30)
    photo = models.ImageField(upload_to='images/')
