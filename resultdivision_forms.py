from django import forms
from .models import ResultDivision


class ResDivisionForm(forms.ModelForm):
    class Meta:
        model = ResultDivision
        fields = ('res_name','res_code',)