from django.views.generic import TemplateView
from django.shortcuts import render, redirect,get_object_or_404
from dashboard.form import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import ModelForm
from .models import Thana
from .thana_forms import*


class IndexView(TemplateView):
    template_name = "components/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({'title': "Welcome"})
        return context




class LoginView(TemplateView):
    template_name = "components/login.html"

    def user_login(request):
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print("user")
        if user:

            if user.is_active:
                 print ("Login details: {0}".format(user))
                 return render(request,'components/index.html',{})

            else:
                print ("Login details: {0}".format(user))
                return HttpResponse("Your account is disabled.")
        else:

          print ("Invalid login details:{0}".format(user))
          return HttpResponse("Invalid login details supplied.")

     else:
         return render(request, 'components/login.html',{})



def thana_list(request,template_name='components/thana.html'):
    th = Thana.objects.all()
    data = {}
    data['object_list'] = th
    return render(request, template_name, data)

def thana_create(request, template_name='components/thana_form.html'):
    form = ThanaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('thana.html')
    return render(request, template_name, {'form':form})

def thana_update(request, pk, template_name='components/thana_form.html'):
    th = get_object_or_404(Thana, pk=pk)
    form = ThanaForm(request.POST or None, instance=th)
    if form.is_valid():
        form.save()
        return redirect('thana.html')
    return render(request, template_name, {'form':form})

def thana_delete(request, pk, template_name='components/thana_confirm_delete.html'):
    th = get_object_or_404(Thana, pk=pk)
    if request.method=='POST':
        th.delete()
        return redirect('thana.html')
    return render(request, template_name, {'object':th})

def thana_view(request,pk, template_name='components/thana_view.html'):
    th = get_object_or_404(Thana, pk=pk)
    form = ThanaForm( None, instance=th)
    return render(request, template_name, {'form':form})


def thana_redirect(request,pk,template_name='components/thana.html'):
    th = Thana.objects.all()
    data = {}
    data['object_list'] = th
    return render(request, template_name, data)





