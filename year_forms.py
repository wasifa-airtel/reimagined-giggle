from django import forms
from .models import Year

class YearForm(forms.ModelForm):
    class Meta:
        model = Year
        fields = ('name','year_code',)

