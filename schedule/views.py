from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy

from schedule.models import Log
from schedule.forms import LogForm

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
