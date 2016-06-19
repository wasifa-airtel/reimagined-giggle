from django import forms
from .division_model import Division


class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ('name','division_code',)