from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404


from horses.models import Horse, MedicalRecord, Task, Log
from horses.forms import HorseForm, MedicalRecordForm, TaskForm, LogForm

from core.mixins import AjaxResponseMixin

# ====================================================================
# Horse
# ====================================================================

class HorseList(ListView):
    model            = Horse
    context_obj_name = 'horse_list'

class HorseCreate(SuccessMessageMixin, CreateView):
    model           = Horse
    form_class      = HorseForm
    success_message = "%(name)s was created successfully."

    def get_context_data(self, **kwargs):
        context = super(HorseCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add a New Horse'
        return context

class HorseDetail(DetailView):
    model            = Horse
    context_obj_name = 'horse'

    def get_context_data(self, **kwargs):
        context = super(HorseDetail, self).get_context_data(**kwargs)
        context['tasks']   = Task.objects.filter(horse_id__exact=self.object.id)
        context['logs']   = Log.objects.filter(horse_id__exact=self.object.id)
        context['records'] = MedicalRecord.objects.filter(horse_id__exact=self.object.id)
        return context

class HorseTaskList(ListView):
    def get_queryset(self):
        self.horse = get_object_or_404(Horse, pk=self.kwargs['pk'])
        return Task.objects.filter(horse=self.horse)

    def get_context_data(self, **kwargs):
        context = super(HorseTaskList, self).get_context_data(**kwargs)
        context['horse'] = self.horse
        return context

class HorseUpdate(SuccessMessageMixin, UpdateView):
    model            = Horse
    form_class       = HorseForm
    success_message  = "%(name)s was updated successfully."

    def get_context_data(self, **kwargs):
        context = super(HorseUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit %s\'s profile' % self.object.name
        return context

class HorseDelete(SuccessMessageMixin, DeleteView):
    model           = Horse
    success_message = 'The Horse was removed successfully.'
    success_url     = reverse_lazy('horse_list')


# ====================================================================
# Tasks
# ====================================================================

class TaskList(ListView):
    model            = Task
    context_obj_name = 'task_list'

class TaskCreate(SuccessMessageMixin, CreateView):
    model           = Task
    form_class      = TaskForm
    success_message = 'The Task was created successfully.'

    def get_context_data(self, **kwargs):
        context = super(TaskCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add a New Task'
        return context

class TaskDetail(DetailView):
    model            = Task
    context_obj_name = 'task'

class TaskUpdate(SuccessMessageMixin, UpdateView):
    model            = Task
    form_class       = TaskForm
    success_message  = 'The Task was updated successfully.'

    def get_context_data(self, **kwargs):
        context = super(TaskUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit %s\'s Task' % self.object.horse.name
        return context

class TaskDelete(SuccessMessageMixin, DeleteView):
    model           = Task
    success_message = 'Task deletion was successfull.'
    success_url     = reverse_lazy('horse_list')


# ====================================================================
# Log
# ====================================================================

class LogCreate(SuccessMessageMixin, CreateView):
    model           = Log
    form_class      = LogForm
    success_message = 'The Log was created successfully.'

    def get_context_data(self, **kwargs):
        context = super(LogCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add a New Log'
        return context

    def get_success_url(self):
        return reverse('horse_detail',args=(self.object.horse.id,))

class LogDelete(SuccessMessageMixin, DeleteView):
    model           = Log
    success_message = 'The Log was deleted successfully.'
    success_url     = reverse_lazy('horse_list')


# ====================================================================
# MedicalRecord
# ====================================================================

class MedicalRecordCreate(SuccessMessageMixin, CreateView):
    model           = MedicalRecord
    form_class      = MedicalRecordForm
    success_message = 'The Medical Record was created successfully.'

    def get_context_data(self, **kwargs):
        context = super(MedicalRecordCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add a New Medical Record'
        return context

    def get_success_url(self):
        return reverse('horse_detail',args=(self.object.horse.id,))

class MedicalRecordUpdate(SuccessMessageMixin, UpdateView):
    model            = MedicalRecord
    form_class       = MedicalRecordForm
    success_message  = 'The Medical Record was updated successfully.'

    def get_context_data(self, **kwargs):
        context = super(MedicalRecordUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit %s\'s Medical Record' % self.object.horse.name
        return context

class MedicalRecordDelete(SuccessMessageMixin, DeleteView):
    model           = MedicalRecord
    success_message = 'The Medical Record was deleted successfully.'
    success_url     = reverse_lazy('horse_list')