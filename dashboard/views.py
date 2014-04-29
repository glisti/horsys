from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin

from dashboard.models import DashboardMessage
from dashboard.forms  import DashboardMessageForm

# ====================================================================
# Dashboard
# ====================================================================

class Dashboard(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['recent_horse_logs']  = None
        context['upcoming_tasks']     = None
        context['dashboard_messages'] = None
        return context

# ====================================================================
# Dashboard Message
# ====================================================================

class DashboardMessageList(ListView):
    model            = DashboardMessage
    context_obj_name = 'message_list'

class DashboardMessageCreate(SuccessMessageMixin, CreateView):
    model           = DashboardMessage
    form_class      = DashboardMessageForm
    success_url     = reverse('dashboard')
    success_message = "The dashboard message was created successfully."

    def get_context_data(self, **kwargs):
        context = super(DashboardMessageCreate, self).get_context_data(**kwargs)
        context['title'] = 'Create a Dashboard Message'
        return context

class DashboardMessageDelete(SuccessMessageMixin, DeleteView):
    model           = DashboardMessage
    success_url     = reverse('dashboard')
    success_message = 'The dashboard message was successfully deleted.'