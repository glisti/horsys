from django.conf.urls import patterns, url
from dashboard.views import *

urlpatterns = patterns('',
    url(r'^$', Dashboard.as_view(), name='dashboard'),
    url(r'^messages/$', DashboardMessageList.as_view(), name='messages'),
    url(r'^message/add/$', DashboardMessageCreate.as_view(), name='message_create'),
    url(r'^message/(?P<pk>\d+)/delete/$', DashboardMessageDelete.as_view(), name='message_delete'),
)
