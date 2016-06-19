from django import forms
from .models import DegreeGeneral


class DegreeGeneralForm(forms.ModelForm):
    class Meta:
        model = DegreeGeneral
        fields = ('name','degreeGeneral_code',)