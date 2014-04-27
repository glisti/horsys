from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from schedule.models import Shift
from schedule.forms import ShiftAMForm, ShiftPMForm

class ShiftList(ListView):
    model            = Shift
    context_obj_name = 'shift_list'

class ShiftAMCreate(SuccessMessageMixin, CreateView):
    model           = Shift
    form_class      = ShiftAMForm
    success_url     = reverse_lazy('shift_list')
    success_message = 'AM Shift Created Successfully.'

    def get_context_data(self, **kwargs):
        context = super(ShiftAMCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add a New AM Shift'
        return context

    def form_valid(self, form):
        form.instance.time_of_day = 'AM'
        return super(ShiftAMCreate, self).form_valid(form)

class ShiftPMCreate(SuccessMessageMixin, CreateView):
    model           = Shift
    form_class      = ShiftPMForm
    success_url     = reverse_lazy('shift_list')
    success_message = 'PM Shift Created Successfully.'

    def get_context_data(self, **kwargs):
        context = super(ShiftPMCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add a New PM Shift'
        return context

    def form_valid(self, form):
        form.instance.time_of_day = 'PM'
        return super(ShiftPMCreate, self).form_valid(form)

class ShiftDetail(DetailView):
    model            = Shift
    context_obj_name = 'shift'

class ShiftAMUpdate(SuccessMessageMixin, UpdateView):
    model           = Shift
    form_class      = ShiftAMForm
    success_message = 'AM Shift Updated Successfully.'

    def get_context_data(self, **kwargs):
        context = super(ShiftAMUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit AM Shift'
        return context

class ShiftPMUpdate(SuccessMessageMixin, UpdateView):
    model           = Shift
    form_class      = ShiftPMForm
    success_message = 'PM Shift Updated Successfully.'

    def get_context_data(self, **kwargs):
        context = super(ShiftPMUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit PM Shift'
        return context

class ShiftDelete(SuccessMessageMixin, DeleteView):
    model       = Shift
    success_url = reverse_lazy('shift_list')

class ScheduleHome(ListView):
    model = Shift
    context_obj_name = 'shift'
    template_name = "schedule/schedule_home.html"

'''
class ClockList(ListView):
    model = Clock
    context_obj_name = 'clock_list'

class ClockCreate(CreateView):
    model = Clock
    form_class = ClockForm
    success_url = reverse_lazy('schedule_home')

class ClockDetail(DetailView):
    model = Clock
    context_obj_name = 'clock'

class ClockUpdate(UpdateView):
    model = Clock
    form_class = ClockForm
    context_obj_name = 'clocks'

class ClockDelete(DeleteView):
    model = Clock
    success_url = reverse_lazy('schedule_home')
'''