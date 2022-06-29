from operator import mod
from statistics import mode
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Alert(models.Model):
    alert_value=models.FloatField(null=True,blank=True)
    status=models.CharField(max_length=10,null=True,blank=True)
    coin=models.CharField(max_length=20,null=True,blank=True)
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.alert_value)