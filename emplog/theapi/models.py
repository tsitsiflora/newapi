from django.db import models

# Create your models here.
class MobileUsers(models.Model):
    first_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    email = models.EmailField(unique=True, max_length=200)
    ec_number = models.IntegerField(unique=True)
    phone = models.PhoneNumberField(unique=True)
    centre = models.CharField(max_length=250)

