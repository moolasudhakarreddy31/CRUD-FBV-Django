from django.db import models

# Create your models here.

class Employee(models.Model):
    empno=models.IntegerField()
    empname=models.CharField(max_length=233)
    empsal=models.IntegerField()
    empaddress=models.CharField(max_length=244)
