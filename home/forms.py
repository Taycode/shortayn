from django import forms
from home import models


class LinkForm(forms.ModelForm):
    class Meta:
        model = models.Link
        fields = '__all__'
