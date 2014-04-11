from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin

from horses.models import Horse, MedicalRecord, Task, Note
from horses.forms import HorseForm, MedicalRecordForm, TaskForm, NoteForm

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
        context['tasks'] = Task.objects.filter(horse_id__exact=self.object.id)
        context['notes'] = Note.objects.filter(horse_id__exact=self.object.id)
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
    success_message = 'Horse removal was successfull.'
    success_url     = reverse_lazy('horse_list')

# ===== Tasks ===== #

class TaskList(ListView):
    model            = Task
    context_obj_name = 'task_list'

class TaskCreate(SuccessMessageMixin, CreateView):
    model           = Task
    form_class      = TaskForm
    success_message = 'Task creation was successfull.'

class TaskDetail(DetailView):
    model            = Task
    context_obj_name = 'task'

class TaskUpdate(SuccessMessageMixin, UpdateView):
    model            = Task
    form_class       = TaskForm
    context_obj_name = 'tasks'
    success_message  = 'Task update was successfull.'

class TaskDelete(SuccessMessageMixin, DeleteView):
    model           = Task
    success_message = 'Task deletion was successfull.'
    success_url     = reverse_lazy('horse_list')

# ===== Notes ===== #

class NoteCreate(SuccessMessageMixin, CreateView):
    model           = Note
    form_class      = NoteForm
    success_message = 'Note creation was successfull.'

    def get_success_url(self):
        return reverse('horse_detail',args=(self.object.horse.id,))

class NoteDelete(SuccessMessageMixin, DeleteView):
    model           = Note
    success_message = 'Note deletion was successfull.'
    success_url     = reverse_lazy('horse_list')
