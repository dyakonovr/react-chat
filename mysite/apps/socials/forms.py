from .models import SocialsLinks
from django.forms import ModelForm
from django import forms


class VkLink(ModelForm):
    class Meta:
        model = SocialsLinks
        fields = '__all__'
        exclude = ['user']
