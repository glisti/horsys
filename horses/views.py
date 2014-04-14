from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin

from horses.models import Horse, MedicalRecord, Task, Note
from horses.forms import HorseForm, MedicalRecordForm, TaskForm, NoteForm

from core.mixins import AjaxResponseMixin

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
        context['notes']   = Note.objects.filter(horse_id__exact=self.object.id)
        context['records'] = MedicalRecord.objects.filter(horse_id__exact=self.object.id)
        return context

class HorseUpdate(SuccessMessageMixin, UpdateView):
    model            = Horse
    form_class       = HorseForm
    context_obj_name = 'horses'
    success_message  = "%(name)s was updated successfully."

    def get_context_data(self, **kwargs):
        context = super(HorseUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit %s\'s profile' % self.object.name
        return context

class HorseDelete(SuccessMessageMixin, DeleteView):
    model           = Horse
    success_message = 'The Horse was removed successfully.'
    success_url     = reverse_lazy('horse_list')

# ===== Tasks ===== #

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
    context_obj_name = 'tasks'
    success_message  = 'The Task was updated successfully.'

class TaskDelete(SuccessMessageMixin, DeleteView):
    model           = Task
    success_message = 'Task deletion was successfull.'
    success_url     = reverse_lazy('horse_list')

# ===== Notes ===== #

class NoteCreate(SuccessMessageMixin, CreateView):
    model           = Note
    form_class      = NoteForm
    success_message = 'The Note was created successfully.'

    def get_context_data(self, **kwargs):
        context = super(NoteCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add a New Note'
        return context

    def get_success_url(self):
        return reverse('horse_detail',args=(self.object.horse.id,))

class NoteDelete(SuccessMessageMixin, DeleteView):
    model           = Note
    success_message = 'The Note was deleted successfully.'
    success_url     = reverse_lazy('horse_list')

# ===== MedicalRecord ===== #

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

class MedicalRecordDelete(SuccessMessageMixin, DeleteView):
    model           = MedicalRecord
    success_message = 'The Medical Record was deleted successfully.'
    success_url     = reverse_lazy('horse_list')