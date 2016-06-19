from django import forms
from .models import Month

class MonthForm(forms.ModelForm):
    class Meta:
        model = Month
        fields = ('month_name','month_code','month_shortname',)

