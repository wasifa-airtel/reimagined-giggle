from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from dashboard.division_model import Division
from dashboard.division_forms import*

def division_list(request,template_name='components/division.html'):
    div= Division.objects.all()
    data = {}
    data['object_list'] = div
    return render(request, template_name, data)

def division_create(request, template_name='components/division_form.html'):
    form = DivisionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('division.html')
    return render(request, template_name, {'form':form})

def division_update(request, pk, template_name='components/division_form.html'):
    div = get_object_or_404(Division, pk=pk)
    form = DivisionForm(request.POST or None, instance=div)
    if form.is_valid():
        form.save()
        return redirect('division.html')
    return render(request, template_name, {'form':form})

def division_delete(request, pk, template_name='components/division_confirm_delete.html'):
    div = get_object_or_404(Division, pk=pk)
    if request.method=='POST':
        div.delete()
        return redirect('division.html')
    return render(request, template_name, {'object':div})

def division_view(request,pk, template_name='components/division_view.html'):
    div = get_object_or_404(Division, pk=pk)
    form = DivisionForm( None, instance=div)
    return render(request, template_name, {'form':form})


def division_redirect(request,pk,template_name='components/division.html'):
    div = Division.objects.all()
    data = {}
    data['object_list'] = div
    return render(request, template_name, data)
