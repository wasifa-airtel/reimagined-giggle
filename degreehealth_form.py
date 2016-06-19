from django import forms
from .models import DegreeHealth


class DegreeHealthForm(forms.ModelForm):
    class Meta:
        model = DegreeHealth
        fields = ('name','degreeHealth_code',)