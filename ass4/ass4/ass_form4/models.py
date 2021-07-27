from django.db import models

# Create your models here.
class StudentReg(models.Model):
    firstname = models.CharField(max_length=10)
    middlename = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    course = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=10)
    age = models.IntegerField()
    project_url = models.URLField()
    email = models.EmailField()
    phone_num = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    re_password = models.CharField(max_length=20)
    address = models.TextField()


class EmployeeReg(models.Model):
    name = models.CharField(max_length=10)
    company = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField()
    phone_num = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    re_password = models.CharField(max_length=20)
    address = models.TextField()

