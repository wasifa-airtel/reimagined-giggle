from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model =Patient
        fields=('first_name','middle_name','last_name','country_id','division_id','district_id','thana_id','zip_code',
               'Street','mobile_number','email','Date_of_birth','NID','Profession','gender_id','user_name','password'
                )
