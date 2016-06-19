from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import Year
from dashboard.year_forms import*

def year_list(request,template_name='components/year.html'):
    yr= Year.objects.all()
    data = {}
    data['object_list'] = yr
    return render(request, template_name, data)

def year_create(request, template_name='components/year_form.html'):
    form = YearForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('year.html')
    return render(request, template_name, {'form':form})

def year_update(request, pk, template_name='components/year_form.html'):
    yr = get_object_or_404(Year, pk=pk)
    form =YearForm(request.POST or None, instance=yr)
    if form.is_valid():
        form.save()
        return redirect('year.html')
    return render(request, template_name, {'form':form})

def year_delete(request, pk, template_name='components/year_confirm_delete.html'):
    yr = get_object_or_404(Year, pk=pk)
    if request.method=='POST':
        yr.delete()
        return redirect('year.html')
    return render(request, template_name, {'object':yr})

def year_view(request,pk, template_name='components/year_view.html'):
    yr = get_object_or_404(Year, pk=pk)
    form = YearForm( None, instance=yr)
    return render(request, template_name, {'form':form})


def year_redirect(request,pk,template_name='components/year.html'):
    yr = Year.objects.all()
    data = {}
    data['object_list'] = yr
    return render(request, template_name, data)
