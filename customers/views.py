from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy , reverse

from customers.models import ContactInfo, Task
from customers.models import Feeder
from customers.models import Boarder
from customers.forms import BoarderForm
# Create your views here.

class FeederList(ListView):
    model = Feeder
    context_obj_name = 'feeder_list'

class BoarderList(ListView):
    model = Boarder
    context_obj_name = 'boarder_list'   

class BoarderCreate(CreateView):
    model = Boarder
    form_class = BoarderForm
    def get_success_url(self):
        return reverse('boarder_detail',args=(self.object.id,))
    def get_context_data(self, **kwargs):
        context = super(BoarderCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add a New Boarder'
        return context	
		
class BoarderDetail(DetailView):
    model = Boarder
    context_obj_name = 'boarder'
    def get_context_data(self, **kwargs):
        context = super(BoarderDetail, self).get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(boarder_id__exact=self.object.id)
        return context		
