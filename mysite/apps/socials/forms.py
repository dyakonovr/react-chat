from .models import Soc_vars
from django.forms import ModelForm
from django import forms


class VkLink(ModelForm):
    class Meta:
        model = Soc_vars
        fields = '__all__'
        exclude = ['user']
