from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy

from customers.models import ContactInfo, Boarders, Owners
from customers.forms import ContactInfoForm, BoardersForm, OwnersForm

class ContactInfoList(ListView):
    model = ContactInfo
    context_obj_name = 'contact_list'
    
class ContactInfoCreate(CreateView):
    model = ContactInfo
    form_class = ContactInfoForm
    success_url = reverse_lazy('contact_list')


class ContactInfoUpdate(UpdateView):
    model = ContactInfo
    context_obj_name = 'customers'

class ContactInfoDelete(DeleteView):
    model = ContactInfo
    success_url = reverse_lazy('contact_list')


class OwnersList(ListView):
    model = Owners
    context_obj_name = 'owner_list'

class OwnersCreate(CreateView):
    model = Owners
    form_class = OwnersForm
    success_url = reverse_lazy('owner_list')

class OwnersDetail(DetailView):
    model = Owners
    context_obj_name = 'owner'

class OwnersUpdate(UpdateView):
    model = Owners
    context_obj_name = 'customers'

class OwnersDelete(DeleteView):
    model = Owners
    success_url = reverse_lazy('owner_list')


class BoardersList(ListView):
    model = Boarders
    context_obj_name = 'boarder_list'

class BoardersCreate(CreateView):
    model = Boarders
    form_class = BoardersForm
    success_url = reverse_lazy('boarder_list')

class BoardersDetail(DetailView):
    model = Boarders
    context_obj_name = 'boarder'

class BoardersUpdate(UpdateView):
    model = Boarders
    context_obj_name = 'customers'

class BoardersDelete(DeleteView):
    model = Boarders
    success_url = reverse_lazy('boarder_list')





