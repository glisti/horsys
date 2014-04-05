from django.conf.urls import patterns, include, url
from schedule.views import LogList, LogCreate, LogDetail, \
                         LogUpdate, LogDelete
urlpatterns = patterns('',
    url(r'^$', LogList.as_view(), name='log_list'),
    url(r'^add/$', LogCreate.as_view(), name='log_create'),
    url(r'^(?P<pk>\d+)/$', LogDetail.as_view(), name='log_detail'),
    url(r'^(?P<pk>\d+)/update/$', LogUpdate.as_view(), name='log_update'),
    url(r'^(?P<pk>\d+)/delete/$', LogDelete.as_view(), name='log_delete'),
)