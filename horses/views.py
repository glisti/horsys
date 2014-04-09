from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy, reverse

from horses.models import Horse, MedicalRecord, Task
from horses.forms import HorseForm, MedicalRecordForm, TaskForm

class HorseList(ListView):
    model = Horse
    context_obj_name = 'horse_list'

class HorseCreate(CreateView):
    model = Horse
    form_class = HorseForm
    def get_success_url(self):
        return reverse('horse_detail',args=(self.object.id,))
    def get_context_data(self, **kwargs):
        context = super(HorseCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add a New Horse'
        return context

class HorseDetail(DetailView):
    model = Horse
    context_obj_name = 'horse'
    def get_context_data(self, **kwargs):
        context = super(HorseDetail, self).get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(horse_id__exact=self.object.id)
        return context

class HorseUpdate(UpdateView):
    model = Horse
    form_class = HorseForm
    context_obj_name = 'horses'
    def get_context_data(self, **kwargs):
        context = super(HorseUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit %s\'s profile' % self.object.name
        return context

class HorseDelete(DeleteView):
    model = Horse
    success_url = reverse_lazy('horse_list')

# ===== Tasks ===== #

class TaskList(ListView):
    model = Task
    context_obj_name = 'task_list'

class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    def get_success_url(self):
        return reverse('task_detail',args=(self.object.id,))

class TaskDetail(DetailView):
    model = Task
    context_obj_name = 'task'

class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    context_obj_name = 'tasks'

class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('horse_list')