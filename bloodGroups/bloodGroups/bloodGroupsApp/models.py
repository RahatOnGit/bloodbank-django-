from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Donor(models.Model):
    name = models.CharField(max_length=30, null = True)
    phone = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=5)
    house_details = models.CharField(max_length=200 ,  null= True)
    upazila = models.CharField(max_length=30,  null= True)
    district = models.CharField(max_length=30, null= True)
    address = models.CharField(max_length=270)
