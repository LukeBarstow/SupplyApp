from django.forms import ModelForm
from .models import Item
from django import forms

class StatusForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
