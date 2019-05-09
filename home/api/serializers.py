from rest_framework import serializers
from django.contrib.auth.models import User
from home import models


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Link
        exclude = ['user',]


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']