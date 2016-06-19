from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect,get_object_or_404
from dashboard.district_model import District
from dashboard.district_forms import*
from django.views.generic import FormView
from django.http import HttpResponse

def district_list(request,template_name='components/district.html'):
    dis= District.objects.all()
    data = {}
    data['object_list'] = dis
    return render(request, template_name, data)

def district_create(request, template_name='components/district_form.html'):
    form = DistrictForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('district.html')
    return render(request, template_name, {'form':form})



def district_update(request, pk, template_name='components/district_form.html'):
    dis= get_object_or_404(District, pk=pk)
    form = DistrictForm(request.POST or None, instance=dis)
    if form.is_valid():
        form.save()
        return redirect('district.html')
    return render(request, template_name, {'form':form})

def district_delete(request, pk, template_name='components/district_confirm_delete.html'):
    dis = get_object_or_404(District, pk=pk)
    if request.method=='POST':
        dis.delete()
        return redirect('district.html')
    return render(request, template_name, {'object':dis})

def district_view(request,pk, template_name='components/district_view.html'):
    dis = get_object_or_404(District, pk=pk)
    form = DistrictForm( None, instance=dis)
    return render(request, template_name, {'form':form})


def district_redirect(request,pk,template_name='components/district.html'):
    dis= District.objects.all()
    data = {}
    data['object_list'] = dis
    return render(request, template_name, data)

