from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from schedule.models import Shift
from schedule.forms import ShiftAMForm, ShiftPMForm

class ShiftList(ListView):
    model            = Shift
    context_obj_name = 'shift_list'

class ShiftCreate(SuccessMessageMixin, CreateView):
    model           = Shift
    success_url     = reverse_lazy('log_list')
    success_message = 'Shift Created Successfully.'
    form_class = ShiftAMForm

    # def get_context_data(self, **kwargs):
    #     context = super(ShiftCreate, self).get_context_data(**kwargs)
    #     print context['form']
    #     if self.kwargs['time'] == 'PM':
    #         context['title'] = 'Add a New PM Shift'
    #         context['form']  = ShiftPMForm
    #     else:
    #         context['title'] = 'Add a New AM Shift'
    #         context['form']  = ShiftAMForm
    #     print context['form']
    #     return context

    def form_invalid(self,form):
        print form.errors
        return super(ShiftCreate,self).form_invalid(form)

    def form_valid(self, form):
        if self.request.method == 'POST':
            form.instance.time_of_day == self.request.POST['time']
        print self.request.POST['time']
        return super(ShiftCreate, self).form_valid(form)

class ShiftDetail(DetailView):
    model            = Shift
    context_obj_name = 'shift'

class ShiftUpdate(SuccessMessageMixin, UpdateView):
    model           = Shift
    success_message = 'Shift Updated Successfully.'

    def get_context_data(self, **kwargs):
        context = super(ShiftUpdate, self).get_context_data(**kwargs)
        if self.kwargs['time'] == 'PM':
            context['title'] = 'Update PM Shift'
            context['form']  = ShiftPMForm
        else:
            context['title'] ='Update AM Shift'
            context['form']  = ShiftAMForm
        return context

    def form_valid(self, form):
        if self.request.method == 'POST':
            form.instance.time_of_day == self.request.POST['time']
        return super(ShiftUpdate, self).form_valid(form)

class ShiftDelete(SuccessMessageMixin, DeleteView):
    model       = Shift
    success_url = reverse_lazy('shift_list')