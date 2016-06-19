from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import DegreeGeneral
from dashboard.degreeGeneral_forms import*

def degreeGeneral_list(request,template_name='components/degreegeneral.html'):
    d= DegreeGeneral.objects.all()
    data = {}
    data['object_list'] = d
    return render(request, template_name, data)

def degreeGeneral_create(request, template_name='components/degreegeneral_form.html'):
    form = DegreeGeneralForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('degreegeneral.html')
    return render(request, template_name, {'form':form})

def degreeGeneral_update(request, pk, template_name='components/degreegeneral_form.html'):
    d = get_object_or_404(DegreeGeneral, pk=pk)
    form =DegreeGeneralForm(request.POST or None, instance=d)
    if form.is_valid():
        form.save()
        return redirect('degreegeneral.html')
    return render(request, template_name, {'form':form})

def degreeGeneral_delete(request, pk, template_name='components/degreegeneral_confirm_delete.html'):
    d = get_object_or_404(DegreeGeneral, pk=pk)
    if request.method=='POST':
        d.delete()
        return redirect('degreegeneral.html')
    return render(request, template_name, {'object':d})

def degreegeneral_view(request,pk, template_name='components/degreegeneral_view.html'):
    d = get_object_or_404(DegreeGeneral, pk=pk)
    form = DegreeGeneralForm( None, instance=d)
    return render(request, template_name, {'form':form})


def degreegeneral_redirect(request,pk,template_name='components/degreegeneral.html'):
    d = DegreeGeneral.objects.all()
    data = {}
    data['object_list'] = d
    return render(request, template_name, data)
