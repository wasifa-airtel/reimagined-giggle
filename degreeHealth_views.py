from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import DegreeHealth
from .degreehealth_form import*

def degreehealth_list(request,template_name='components/degreeHealth.html'):
    deg= DegreeHealth.objects.all()
    data = {}
    data['object_list'] = deg
    return render(request, template_name, data)

def degreehealth_create(request, template_name='components/degreehealth_form.html'):
    form = DegreeHealthForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('degreeHealth.html')
    return render(request, template_name, {'form':form})

def degreehealth_update(request, pk, template_name='components/degreehealth_form.html'):
    deg= get_object_or_404(DegreeHealth, pk=pk)
    form = DegreeHealthForm(request.POST or None, instance=deg)
    if form.is_valid():
        form.save()
        return redirect('degreeHealth.html')
    return render(request, template_name, {'form':form})

def degreehealth_delete(request, pk, template_name='components/degreehealth_confirm.html'):
    deg =get_object_or_404(DegreeHealth, pk=pk)
    if request.method=='POST':
        deg.delete()
        return redirect('degreeHealth.html')
    return render(request, template_name, {'object':deg})

def degreehealth_view(request,pk, template_name='components/degreeHealth_view.html'):
    deg = get_object_or_404(DegreeHealth, pk=pk)
    form = DegreeHealthForm( None, instance=deg)
    return render(request, template_name, {'form':form})


def degreehealth_redirect(request,pk,template_name='components/degreeHealth.html'):
    deg =DegreeHealth.objects.all()
    data = {}
    data['object_list'] = deg
    return render(request, template_name, data)
