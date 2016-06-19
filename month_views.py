from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import Month
from dashboard.month_forms import*

def month_list(request,template_name='components/month.html'):
    mon= Month.objects.all()
    data = {}
    data['object_list'] = mon
    return render(request, template_name, data)

def month_create(request, template_name='components/month_form.html'):
    form = MonthForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('month.html')
    return render(request, template_name, {'form':form})

def month_update(request, pk, template_name='components/month_form.html'):
    mon = get_object_or_404(Month, pk=pk)
    form =MonthForm(request.POST or None, instance=mon)
    if form.is_valid():
        form.save()
        return redirect('month.html')
    return render(request, template_name, {'form':form})

def month_delete(request, pk, template_name='components/month_confirm_delete.html'):
    mon = get_object_or_404(Month, pk=pk)
    if request.method=='POST':
        mon.delete()
        return redirect('month.html')
    return render(request, template_name, {'object':mon})

def month_view(request,pk, template_name='components/month_view.html'):
    mon = get_object_or_404(Month, pk=pk)
    form = MonthForm( None, instance=mon)
    return render(request, template_name, {'form':form})


def month_redirect(request,pk,template_name='components/month.html'):
    mon = Month.objects.all()
    data = {}
    data['object_list'] = mon
    return render(request, template_name, data)
