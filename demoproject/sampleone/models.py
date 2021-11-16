from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

class Department(models.Model):
    dep_id = models.IntegerField()
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
