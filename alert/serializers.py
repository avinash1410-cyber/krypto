from dataclasses import field
from pyexpat import model
from unittest import mock
from rest_framework import serializers

from alert.models import Alert,User


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model=Alert
        fields=['id','alert_value','status','user','coin']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"