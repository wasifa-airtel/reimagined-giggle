from django.shortcuts import render, redirect,get_object_or_404
from .models import Country
from .country_form import*
from django.views.generic import FormView
from django.http import HttpResponse

def country_list(request,template_name='components/country.html'):
    cou= Country.objects.all()
    data = {}
    data['object_list'] = cou
    return render(request, template_name, data)

def country_create(request, template_name='components/country_form.html'):
    form = CountryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('country.html')
    return render(request, template_name, {'form':form})



def country_update(request, pk, template_name='components/country_form.html'):
    cou= get_object_or_404(Country, pk=pk)
    form = CountryForm(request.POST or None, instance=cou)
    if form.is_valid():
        form.save()
        return redirect('country.html')
    return render(request, template_name, {'form':form})

def country_delete(request, pk, template_name='components/country_confirm_delete.html'):
    cou = get_object_or_404(Country, pk=pk)
    if request.method=='POST':
        cou.delete()
        return redirect('country.html')
    return render(request, template_name, {'object':cou})

def country_view(request,pk, template_name='components/country_view.html'):
    cou = get_object_or_404(Country, pk=pk)
    form = CountryForm( None, instance=cou)
    return render(request, template_name, {'form':form})


def country_redirect(request,pk,template_name='components/country.html'):
    cou= Country.objects.all()
    data = {}
    data['object_list'] = cou
    return render(request, template_name, data)

