from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404


from customers.models import ContactInfo, Boarders, Owners, LiabilityWaiver, BoarderAgreement, ChecksPaid
from customers.forms import ContactInfoForm, BoardersForm, OwnersForm, OwnerContactInfoForm, LiabilityWaiverForm, BoarderAgreementForm, ChecksPaidForm

# ====================================================================
# Contact Information (Owner and Boarder)
# ====================================================================
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
    form_class       = ContactInfoForm
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
    form_class = OwnerContactInfoForm
    context_obj_name = 'customers'
    success_url = reverse_lazy('owner_list')
    def get_context_data(self, **kwargs):
        context = super(OwnerContactInfoUpdate, self).get_context_data(**kwargs)
        context['contacts'] = 'Edit %s\'s  Contact Information' % self.object.owner_name.owner
        return context

class OwnerContactInfoDelete(DeleteView):
    model = ContactInfo
    success_url = reverse_lazy('owner_list')




# ====================================================================
# Owners
# ====================================================================


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
    form_class       = OwnersForm
    context_obj_name = 'customers'
    success_url = reverse_lazy('owner_list')


class OwnersDelete(DeleteView):
    model = Owners
    success_url = reverse_lazy('owner_list')

# ====================================================================
# Boarders
# ====================================================================
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
        context['liab_waivers'] = LiabilityWaiver.objects.filter(boarder_name_id__exact=self.object.id)
        context['checks_paid'] = ChecksPaid.objects.filter(boarder_name_id__exact=self.object.id)
        context['boarder_agreements'] = BoarderAgreement.objects.filter(boarder_name_id__exact=self.object.id)
        return context

class BoardersUpdate(UpdateView):
    model = Boarders
    form_class       = BoardersForm
    context_obj_name = 'customers'
    success_url = reverse_lazy('boarder_list')
    def get_context_data(self, **kwargs):
        context = super(BoardersUpdate, self).get_context_data(**kwargs)
        context['contacts'] = ContactInfo.objects.filter(boarder_name_id__exact=self.object.id)
        return context

class BoardersDelete(DeleteView):
    model = Boarders
    success_url = reverse_lazy('boarder_list')



# ====================================================================
# Boarder Documents
# ChecksPaid, LiabilityWaiver, BoarderAgreement
# ====================================================================

class ChecksPaidCreate(SuccessMessageMixin, CreateView):
    model           = ChecksPaid
    form_class      = ChecksPaidForm
    success_message = 'The Checks Paid Record was created successfully.'

    def get_context_data(self, **kwargs):
        context = super(ChecksPaidCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add a New Checks Paid Record'
        return context

    def get_success_url(self):
        return reverse('boarder_detail',args=(self.object.boarder_name.id,))

class ChecksPaidUpdate(SuccessMessageMixin, UpdateView):
    model            = ChecksPaid
    form_class       = ChecksPaidForm
    success_message  = 'The Checks Paid Record was updated successfully.'

    def get_context_data(self, **kwargs):
        context = super(ChecksPaidUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit %s\'s Checks Paid' % self.object.boarder_name
        return context

class ChecksPaidDelete(SuccessMessageMixin, DeleteView):
    model           = ChecksPaid
    success_message = 'The Checks Paid Record was deleted successfully.'
    success_url     = reverse_lazy('boarder_list')

#############################################################
class LiabilityWaiverCreate(SuccessMessageMixin, CreateView):
    model           = LiabilityWaiver
    form_class      = LiabilityWaiverForm
    success_message = 'The Liability Waiver was created successfully.'

    def get_context_data(self, **kwargs):
        context = super(LiabilityWaiverCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add a New Liability Waiver'
        return context

    def get_success_url(self):
        return reverse('boarder_detail',args=(self.object.boarder_name.id,))

class LiabilityWaiverUpdate(SuccessMessageMixin, UpdateView):
    model            = LiabilityWaiver
    form_class       = LiabilityWaiverForm
    success_message  = 'The Liability Waiver was updated successfully.'

    def get_context_data(self, **kwargs):
        context = super(LiabilityWaiverUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit %s\'s Liability Waiver' % self.object.boarder.boarder
        return context

class LiabilityWaiverDelete(SuccessMessageMixin, DeleteView):
    model           = LiabilityWaiver
    success_message = 'The Liability Waiver was deleted successfully.'
    success_url     = reverse_lazy('boarder_list')

#############################################################
class BoarderAgreementCreate(SuccessMessageMixin, CreateView):
    model           = BoarderAgreement
    form_class      = BoarderAgreementForm
    success_message = 'The Boarder Agreement was created successfully.'

    def get_context_data(self, **kwargs):
        context = super(BoarderAgreementCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add a New Boarder Agreement'
        return context

    def get_success_url(self):
        return reverse('boarder_detail',args=(self.object.boarder_name.id,))

class BoarderAgreementUpdate(SuccessMessageMixin, UpdateView):
    model            = BoarderAgreement
    form_class       = BoarderAgreementForm
    success_message  = 'The Boarder Agreement was updated successfully.'

    def get_context_data(self, **kwargs):
        context = super(BoarderAgreementUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit %s\'s Boarder Agreement' % self.object.boarder.boarder
        return context

class BoarderAgreementDelete(SuccessMessageMixin, DeleteView):
    model           = BoarderAgreement
    success_message = 'The Boarder Agreement was deleted successfully.'
    success_url     = reverse_lazy('boarder_list')            