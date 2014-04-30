from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.utils import timezone

from datetime import timedelta

from dashboard.models import DashboardMessage
from dashboard.forms  import DashboardMessageForm
from horses.models    import Task, Log

# ====================================================================
# Dashboard
# ====================================================================

class Dashboard(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        now                       = timezone.now()
        context['recent_logs']    = Log.objects.filter(created__range=[now-timedelta(days=7),now])
        context['upcoming_tasks'] = Task.objects.filter(date__gte=now).exclude(completed=True)
        context['expired_tasks']  = Task.objects.filter(date__lte=now).exclude(completed=True)
        context['message_feed']   = DashboardMessage.objects.all()[:5]
        return context

class RecentLogs(ListView):
    model = Log
    context_obj_name = 'logs'

    def get_context_data(self, **kwargs):
        context = super(RecentLogs, self).get_context_data(**kwargs)
        now                    = timezone.now()
        context['recent_logs'] = Log.objects.filter(created__range=[now-timedelta(days=7),now])
        return context

class UpcomingTasks(ListView):
    model = Log
    context_obj_name = 'logs'

    def get_context_data(self, **kwargs):
        context = super(UpcomingTasks, self).get_context_data(**kwargs)
        now                       = timezone.now()
        context['upcoming_tasks'] = Task.objects.filter(date__gte=now).exclude(completed=True)
        return context

class ExpiredTasks(ListView):
    model = Log
    context_obj_name = 'logs'

    def get_context_data(self, **kwargs):
        context = super(ExpiredTasks, self).get_context_data(**kwargs)
        now                      = timezone.now()
        context['expired_tasks'] = Task.objects.filter(date__lte=now).exclude(completed=True)
        return context

# ====================================================================
# Dashboard Message
# ====================================================================

class DashboardMessageList(ListView):
    model            = DashboardMessage
    context_obj_name = 'messages'

class DashboardMessageCreate(SuccessMessageMixin, CreateView):
    model           = DashboardMessage
    form_class      = DashboardMessageForm
    success_url     = reverse_lazy('dashboard')
    success_message = "The dashboard message was created successfully."

    def get_context_data(self, **kwargs):
        context = super(DashboardMessageCreate, self).get_context_data(**kwargs)
        context['title'] = 'Create a Dashboard Message'
        return context

class DashboardMessageDelete(SuccessMessageMixin, DeleteView):
    model           = DashboardMessage
    success_url     = reverse_lazy('dashboard')
    success_message = 'The dashboard message was successfully deleted.'