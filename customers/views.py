from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy, reverse

from customers.models import ContactInfo, Boarders, Owners
from customers.forms import ContactInfoForm, BoardersForm, OwnersForm, OwnerContactInfoForm


class ContactInfoList(ListView):
    model = ContactInfo
    context_obj_name = 'contact_list'

    
class ContactInfoCreate(CreateView):
    model = ContactInfo
    form_class = ContactInfoForm
    #success_url = reverse_lazy('boarders_detail')
    def get_success_url(self):
        return reverse('boarder_detail',args=(self.object.boarder_name.id,))

class ContactInfoUpdate(UpdateView):
    model = ContactInfo
    context_obj_name = 'customers'
    def get_context_data(self, **kwargs):
        context = super(ContactInfoUpdate, self).get_context_data(**kwargs)
        context['contacts'] = 'Edit %s\'s  Contact Information' % self.object.boarder_name.boarder
        return context

class ContactInfoDelete(DeleteView):
    model = ContactInfo
    success_url = reverse_lazy('contact_list')

class OwnerContactInfoList(ListView):
    model = ContactInfo
    context_obj_name = 'contact_list'

    
class OwnerContactInfoCreate(CreateView):
    model = ContactInfo
    form_class = OwnerContactInfoForm
    #success_url = reverse_lazy('boarders_detail')
    def get_success_url(self):
        return reverse('owner_detail',args=(self.object.owner_name.id,))

class OwnerContactInfoUpdate(UpdateView):
    model = ContactInfo
    context_obj_name = 'customers'
    def get_context_data(self, **kwargs):
        context = super(OwnerContactInfoUpdate, self).get_context_data(**kwargs)
        context['contacts'] = 'Edit %s\'s  Contact Information' % self.object.owner_name.owner
        return context

class OwnerContactInfoDelete(DeleteView):
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
    def get_context_data(self, **kwargs):
        context = super(OwnersDetail, self).get_context_data(**kwargs)
        context['contacts'] = ContactInfo.objects.filter(owner_name_id__exact=self.object.id)
        return context


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
    def get_context_data(self, **kwargs):
        context = super(BoardersDetail, self).get_context_data(**kwargs)
        context['contacts'] = ContactInfo.objects.filter(boarder_name_id__exact=self.object.id)
        return context

class BoardersUpdate(UpdateView):
    model = Boarders
    context_obj_name = 'customers'
    

class BoardersDelete(DeleteView):
    model = Boarders
    success_url = reverse_lazy('boarder_list')


