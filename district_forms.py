from django import forms
from .district_model import District

class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ('name','district_code','division_id',)

