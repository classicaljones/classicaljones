from django import forms
from products import models

class MakeDetail(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['name', 'email']