from django.db import models

# Create your models here.
class ScholoshipReg(models.Model):
    firstname = models.CharField(max_length=10)
    middlename = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    scholorship_catagory = models.CharField(max_length=10)
    College = models.CharField(max_length=10)
    aadhar_number = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField()
    phone_num = models.CharField(max_length=10)
    address = models.TextField()