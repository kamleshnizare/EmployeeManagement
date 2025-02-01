from django.db import models

# Create your models here.
class EmployeeInfo(models.Model):
    ename = models.CharField(max_length=85)
    eage = models.IntegerField()
    esal = models.FloatField()
    eadd = models.CharField(max_length=85)