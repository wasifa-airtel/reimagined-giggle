from django import forms
from .district_model import District
from .division_model import Division
from .models import Thana


class ThanaForm(forms.ModelForm):
    class Meta:
        model = Thana
        fields = ['name','thana_code','division_id','district_id']
