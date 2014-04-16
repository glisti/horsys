from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy

from schedule.models import Shift, Clock
from schedule.forms import ShiftForm, ClockForm

class ShiftList(ListView):
    model = Shift
    context_obj_name = 'shift_list'

class ShiftCreate(CreateView):
    model = Shift
    form_class = ShiftForm
    success_url = reverse_lazy('schedule_home')

class ShiftDetail(DetailView):
    model = Shift
    context_obj_name = 'shift'

# class ShiftUpdate(UpdateView):
#     model = Shift
#     context_obj_name = 'shiftAMs'

class ShiftDelete(DeleteView):
    model = Shift
    success_url = reverse_lazy('schedule_home')


class ScheduleHome(ListView):
    model = Shift
    context_obj_name = 'shift'
    template_name = "schedule/schedule_home.html"

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

# class ShiftUpdate(UpdateView):
#     model = Shift
#     context_obj_name = 'shiftAMs'

class ClockDelete(DeleteView):
    model = Clock
    success_url = reverse_lazy('schedule_home')
