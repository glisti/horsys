from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy

from schedule.models import Log, ShiftAM, ShiftPM
from schedule.forms import LogForm, ShiftAMForm, ShiftPMForm

class LogList(ListView):
    model = Log
    context_obj_name = 'log_list'

class LogCreate(CreateView):
    model = Log
    form_class = LogForm
    success_url = reverse_lazy('log_list')

class LogDetail(DetailView):
    model = Log
    context_obj_name = 'log'

class LogUpdate(UpdateView):
    model = Log
    context_obj_name = 'logs'

class LogDelete(DeleteView):
    model = Log
    success_url = reverse_lazy('log_list')


class ShiftAMList(ListView):
    model = ShiftAM
    context_obj_name = 'shiftAM_list'

    def get_context_data(self, **kwargs):
        ctx = super(ShiftAMList, self).get_context_data(**kwargs)
        ctx['shiftpm_list'] = ShiftPM.objects.all()
        return ctx

class ShiftAMCreate(CreateView):
    model = ShiftAM
    form_class = ShiftAMForm
    success_url = reverse_lazy('log_list')

class ShiftAMDetail(DetailView):
    model = ShiftAM
    context_obj_name = 'shiftAM'

class ShiftAMUpdate(UpdateView):
    model = ShiftAM
    context_obj_name = 'shiftAMs'

class ShiftAMDelete(DeleteView):
    model = ShiftAM
    success_url = reverse_lazy('shiftAM_list')

class ShiftPMCreate(CreateView):
    model = ShiftPM
    form_class = ShiftPMForm
    success_url = reverse_lazy('log_list')

class ShiftPMDetail(DetailView):
    model = ShiftPM
    context_obj_name = 'shiftPM'

class ShiftPMUpdate(UpdateView):
    model = ShiftPM
    context_obj_name = 'shiftPMs'

class ShiftPMDelete(DeleteView):
    model = ShiftAM
    success_url = reverse_lazy('shiftAM_list')
