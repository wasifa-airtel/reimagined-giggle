from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import Day
from dashboard.day_forms import*

def day_list(request,template_name='components/day.html'):
    day= Day.objects.all()
    data = {}
    data['object_list'] = day
    return render(request, template_name, data)

def day_create(request, template_name='components/day_form.html'):
    form = DayForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('day.html')
    return render(request, template_name, {'form':form})

def day_update(request, pk, template_name='components/day_form.html'):
    day = get_object_or_404(Day, pk=pk)
    form =DayForm(request.POST or None, instance=day)
    if form.is_valid():
        form.save()
        return redirect('day.html')
    return render(request, template_name, {'form':form})

def day_delete(request, pk, template_name='components/day_confirm_delete.html'):
    day = get_object_or_404(Day, pk=pk)
    if request.method=='POST':
        day.delete()
        return redirect('day.html')
    return render(request, template_name, {'object':day})

def day_view(request,pk, template_name='components/day_view.html'):
    day = get_object_or_404(Day, pk=pk)
    form = DayForm( None, instance=day)
    return render(request, template_name, {'form':form})


def day_redirect(request,pk,template_name='components/day.html'):
    day = Day.objects.all()
    data = {}
    data['object_list'] = day
    return render(request, template_name, data)
