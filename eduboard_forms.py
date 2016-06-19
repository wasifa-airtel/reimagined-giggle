from django import forms
from .models import EduBoard


class EduBoardForm(forms.ModelForm):
    class Meta:
        model = EduBoard
        fields = ('edu_name','edu_code',)