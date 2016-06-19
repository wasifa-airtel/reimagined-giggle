from django.shortcuts import render, redirect,get_object_or_404
from .models import Gender
from .gender_form import*
from django.views.generic import FormView
from django.http import HttpResponse


def gender_list(request,template_name='components/gender.html'):
    gen= Gender.objects.all()
    data = {}
    data['object_list'] = gen
    return render(request, template_name, data)

def gender_create(request,template_name='components/gender_form.html'):
    form = GenderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gender.html')
    return render(request, template_name, {'form':form})

def gender_update(request,pk,template_name='components/gender_form.html'):
    gen=get_object_or_404(Gender,pk=pk)
    form=GenderForm(request.POST or None,instance=gen)
    if form.is_valid():
        form.save()
        return redirect ('gender.html')
    return render(request,template_name ,{'form':form})


def gender_delete(request,pk,template_name ='components/gender_confirm_delete.html' ):
    gen=get_object_or_404(Gender,pk=pk)
    if request.method == 'POST':
        gen.delete()
        return redirect('gender.html')
    return render(request, template_name, {'object':gen})


def gender_view(request,pk, template_name='components/gender_view.html'):
    gen = get_object_or_404(Gender, pk=pk)
    form = GenderForm( None, instance=gen)
    return render(request, template_name, {'form':form})


def gender_redirect(request,pk,template_name='components/gender.html'):
    gen= Gender.objects.all()
    data = {}
    data['object_list'] = gen
    return render(request, template_name, data)



