from django.shortcuts import render, redirect,get_object_or_404
from .models import Patient
from .patient_forms import *
from django.views.generic import FormView
from django.http import HttpResponse

def patient_list(request,template_name='components/patient.html'):
    pat= Patient.objects.all()
    data={}
    data['object_list']= pat
    return render(request,template_name,data)

def patient_create(request,template_name='components/patient_form.html'):
    form=PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('patient.html')
    return render(request,template_name,{'form':form})

def patient_update(request,pk,template_name='components/patient_form.html'):
    pat=get_object_or_404(Patient,pk=pk)
    form=PatientForm(request.POST or None,instance=pat)
    if form.is_valid():
        form.save()
        return redirect('patient.html')
    return render(request,template_name,{'form':form})

def patient_delete(request,pk,template_name='components/patient_confirm_delete.html'):
    pat = get_object_or_404(Patient,pk=pk)
    if request.method=='POST':
        pat.delete()
        return redirect('patient.html')
    return render(request,template_name,{'Object':pat})

def patient_view(request,pk, template_name='components/patient_view.html'):
    pat = get_object_or_404(Patient, pk=pk)
    form = PatientForm( None, instance=pat)
    return render(request, template_name, {'form':form})

def patient_redirect(request,pk,template_name='components/patient.html'):
    pat= Patient.objects.all()
    data = {}
    data['object_list'] = pat
    return render(request, template_name, data)



