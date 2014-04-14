from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy

from schedule.models import Shift
from schedule.forms import ShiftAMForm, ShiftPMForm

class ShiftList(ListView):
    model = Shift
    context_obj_name = 'shift_list'

class ShiftAMCreate(CreateView):
    model = Shift
    form_class = ShiftAMForm
    success_url = reverse_lazy('log_list')

class ShiftPMCreate(CreateView):
    model = Shift
    form_class = ShiftPMForm
    success_url = reverse_lazy('log_list')

class ShiftDetail(DetailView):
    model = Shift
    context_obj_name = 'shif'

# class ShiftUpdate(UpdateView):
#     model = Shift
#     context_obj_name = 'shiftAMs'

class ShiftDelete(DeleteView):
    model = Shift
    success_url = reverse_lazy('shift_list')