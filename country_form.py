from django import forms
from .models import Country



class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('name','country_code',)