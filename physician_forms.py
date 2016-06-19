from django import forms
from django.forms.models import inlineformset_factory
from .models import Physician,PhysicianEduHealthMapping,PhysicianTraining, PhysicianEduQualification,PhysicianProfessional



class PhysicianForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model =Physician
        fields=['first_name','middle_name','last_name','country_id','division_id','district_id','thana_id','zip_code',
               'Street','mobile_number','email','Date_of_birth','NID','Profession','gender_id','user_name','password']


class DegreeForm(forms.ModelForm):
    class Meta:
        model=PhysicianEduHealthMapping
        fields=['physician_id','degree_edu_health_id','country_id','institute','year_id','ref_no']


class TrainingForm(forms.ModelForm):
    class Meta:
        model= PhysicianTraining
        fields=['training_course','country_id','institute','year_id','ref_no']

class EduQualificationForm(forms.ModelForm):
    class Meta:
        model=  PhysicianEduQualification
        fields=['degree','country_id','Education_Board','institute','year_id','Result_Division','Result_CGPA','CGPA_Scale','Ref_no']

class PhysicianProfessionalForm(forms.ModelForm):
    class Meta:
        model= PhysicianProfessional
        fields=[ 'Role','Organization','country_id','start_date','end_date','Ref_no']




PhysicianFormSet = inlineformset_factory(Physician,PhysicianEduHealthMapping,extra=0, min_num=1, fields=('physician_id','degree_edu_health_id','country_id','institute','year_id','ref_no',))
TrainingFormSet = inlineformset_factory(Physician,PhysicianTraining,extra=0, min_num=1, fields=('training_course','country_id','institute','year_id','ref_no',))
EduQualificationFormSet = inlineformset_factory(Physician, PhysicianEduQualification,extra=0, min_num=1, fields=('degree','country_id','Education_Board','institute','year_id','Result_Division','Result_CGPA','CGPA_Scale','Ref_no',))
PhysicianProfessionalFormSet=inlineformset_factory(Physician, PhysicianProfessional,extra=0, min_num=1, fields=('Role','Organization','country_id','start_date','end_date','Ref_no',))
