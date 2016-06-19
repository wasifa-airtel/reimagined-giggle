from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import EduBoard
from .eduboard_forms import*

def eduboard_list(request,template_name='components/eduboard.html'):
    edu= EduBoard.objects.all()
    data = {}
    data['object_list'] = edu
    return render(request, template_name, data)

def eduboard_create(request, template_name='components/eduboard_form.html'):
    form = EduBoardForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('eduboard.html')
    return render(request, template_name, {'form':form})

def eduboard_update(request, pk, template_name='components/eduboard_form.html'):
    edu = get_object_or_404(EduBoard, pk=pk)
    form =EduBoardForm(request.POST or None, instance=edu)
    if form.is_valid():
        form.save()
        return redirect('eduboard.html')
    return render(request, template_name, {'form':form})

def eduboard_delete(request, pk, template_name='components/eduboard_confirm_delete.html'):
    edu = get_object_or_404(EduBoard, pk=pk)
    if request.method=='POST':
        edu.delete()
        return redirect('eduboard.html')
    return render(request, template_name, {'object':edu})

def eduboard_view(request,pk, template_name='components/eduboard_view.html'):
    edu = get_object_or_404(EduBoard, pk=pk)
    form = EduBoardForm( None, instance=edu)
    return render(request, template_name, {'form':form})


def eduboard_redirect(request,pk,template_name='components/eduboard.html'):
    edu= EduBoard.objects.all()
    data = {}
    data['object_list'] = edu
    return render(request, template_name, data)
