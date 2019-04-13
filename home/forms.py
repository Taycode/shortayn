from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from home import models


class LinkForm(forms.ModelForm):
    class Meta:
        model = models.Link
        exclude = ('amount_of_visits', )


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
