from django.db import models

# Create your models here.
class MobileUsers(models.Model):
    first_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    ec_number = models.IntegerField()
    phone = models.IntegerField()
    centre = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name