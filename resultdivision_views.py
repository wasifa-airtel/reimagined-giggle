from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import ResultDivision
from .resultdivision_forms import*

def resultdvision_list(request,template_name='components/resdiv.html'):
    res= ResultDivision.objects.all()
    data = {}
    data['object_list'] = res
    return render(request, template_name, data)

def resultdivision_create(request, template_name='components/resdiv_form.html'):
    form = ResDivisionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('resdiv.html')
    return render(request, template_name, {'form':form})

def resultdivision_update(request, pk, template_name='components/resdiv_form.html'):
    res = get_object_or_404(ResultDivision, pk=pk)
    form =ResDivisionForm(request.POST or None, instance=res)
    if form.is_valid():
        form.save()
        return redirect('resdiv.html')
    return render(request, template_name, {'form':form})

def resultdivision_delete(request, pk, template_name='components/resdiv_confirm_delete.html'):
    res = get_object_or_404(ResultDivision, pk=pk)
    if request.method=='POST':
        res.delete()
        return redirect('resdiv.html')
    return render(request, template_name, {'object':res})

def resultdivision_view(request,pk, template_name='components/resdiv_view.html'):
    res = get_object_or_404(ResultDivision, pk=pk)
    form = ResDivisionForm( None, instance=res)
    return render(request, template_name, {'form':form})


def resultdivision_redirect(request,pk,template_name='components/resdiv.html'):
    res= ResultDivision.objects.all()
    data = {}
    data['object_list'] = res
    return render(request, template_name, data)
