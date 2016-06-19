from django import forms
from .models import Day

class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ('day_name',)

