from django.shortcuts import render, redirect,get_object_or_404,render_to_response
from .models import Physician ,PhysicianEduHealthMapping,PhysicianTraining
from .physician_forms import PhysicianForm, PhysicianFormSet,TrainingFormSet,EduQualificationFormSet,PhysicianProfessionalFormSet
from django.views.generic import FormView
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DetailView, UpdateView



class FormsetMixin(object):
    print 'FormsetMixin Object'
    #object = None

    def get(self, request, *args, **kwargs):
        self.object=None #New

        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        degree_form=PhysicianFormSet() #New
        training_form=TrainingFormSet() #New
        edu_form= EduQualificationFormSet()
        physician_professional_form=PhysicianProfessionalFormSet()

        #formset_class = self.get_formset_class()
        #formset_class = self.get_formset_class()
        #formset = self.get_formset(formset_class)

        #return self.render_to_response(self.get_context_data(form=form, formset=formset))
        return self.render_to_response(self.get_context_data(form=form, degree_form=degree_form,training_form=training_form ,edu_form=edu_form,physician_professional_form=physician_professional_form))

    def post(self, request, *args, **kwargs):
        self.object=None #New

        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        degree_form=PhysicianFormSet(self.request.POST) #New
        training_form=TrainingFormSet(self.request.POST) #New
        edu_form= EduQualificationFormSet(self.request.POST)
        physician_professional_form=PhysicianProfessionalFormSet(self.request.POST)

        #formset_class = self.get_formset_class()
        #formset = self.get_formset(formset_class)

        #if form.is_valid() and formset.is_valid():
        #    return self.form_valid(form, formset)
        #else:
        #    return self.form_invalid(form, formset)

        if form.is_valid() and degree_form.is_valid() and training_form.is_valid()and edu_form.is_valid()and physician_professional_form.is_valid():
            return self.form_valid(form, degree_form,training_form,edu_form,physician_professional_form)
        else:
            return self.form_invalid(form, degree_form,training_form,edu_form,physician_professional_form)


    def get_formset_class(self):
        return self.formset_class

    def get_formset(self, formset_class):
        return formset_class(**self.get_formset_kwargs())

    def get_formset_kwargs(self):
        kwargs = {
            'instance': self.object
        }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def form_valid(self, form, degree_form,training_form,edu_form,physician_professional_form):
        self.object = form.save()

        #formset.instance = self.object
        #formset.save()
        degree_form.instance=self.object #New
        degree_form.save() #New

        training_form.instance=self.object #New
        training_form.save() #New


        edu_form.instance=self.object #New
        edu_form.save() #New


        physician_professional_form.instance=self.object #New
        physician_professional_form.save() #New

        return redirect('physician.html')

    def form_invalid(self, form, degree_form,training_form,edu_form,physician_professional_form):
        #return self.render_to_response(self.get_context_data(form=form, formset=formset))
         return self.render_to_response(self.get_context_data(form=form, degree_form=degree_form,training_form=training_form ,edu_form=edu_form,physician_professional_form=physician_professional_form))



#To Create the add form
class PhysicianCreateView(FormsetMixin,CreateView):
    template_name = 'components/physician_form.html'
    model = Physician
    form_class = PhysicianForm
    formset_class = PhysicianFormSet


#Dont look down
class PhysicianUpdateView(FormsetMixin, UpdateView):
    template_name = 'components/physician_edit.html'
    is_update_view = True
    model = Physician
    form_class = PhysicianForm
    formset_class = PhysicianFormSet


class PhysicianView(FormsetMixin, UpdateView):
    template_name = 'components/physician_view.html'
    is_update_view = True
    model = Physician
    form_class = PhysicianForm
    formset_class = PhysicianFormSet

def physician_list(request,template_name='components/physician.html'):
    phy= Physician.objects.all()
    data={}
    data['object_list']= phy
    return render(request,template_name,data)


def physician_delete(request,pk,template_name='components/physician_confirm_delete.html'):
    phy = get_object_or_404(Physician,pk=pk)
    if request.method=='POST':
        phy.delete()
        return redirect('physician.html')
    return render(request,template_name,{'Object':phy})


def physician_redirect(request,pk,template_name='components/physician.html'):
    phy= Physician.objects.all()
    data = {}
    data['object_list'] =phy
    return render(request, template_name, data)



