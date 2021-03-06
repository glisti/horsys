from django.conf.urls import patterns, include, url
from horses.views import *

urlpatterns = patterns('',
    url(r'^$', HorseList.as_view(), name='horse_list'),

    url(r'^add/$', HorseCreate.as_view(), name='horse_create'),
    url(r'^(?P<pk>\d+)/$', HorseDetail.as_view(), name='horse_detail'),
    url(r'^(?P<pk>\d+)/update/$', HorseUpdate.as_view(), name='horse_update'),
    url(r'^(?P<pk>\d+)/delete/$', HorseDelete.as_view(), name='horse_delete'),

    url(r'^(?P<pk>\d+)/tasks/$', HorseTaskList.as_view(), name='horsetask_list'),

    url(r'^task/add/$', TaskCreate.as_view(), name='task_create'),
    url(r'^task/(?P<pk>\d+)/$', TaskDetail.as_view(), name='task_detail'),
    url(r'^task/(?P<pk>\d+)/update/$', TaskUpdate.as_view(), name='task_update'),
    url(r'^task/(?P<pk>\d+)/delete/$', TaskDelete.as_view(), name='task_delete'),

    url(r'^log/add/$', LogCreate.as_view(), name='log_create'),
    url(r'^log/(?P<pk>\d+)/delete/$', LogDelete.as_view(), name='log_delete'),

    url(r'^record/add/$', MedicalRecordCreate.as_view(), name='record_create'),
    url(r'^record/(?P<pk>\d+)/update/$', MedicalRecordUpdate.as_view(), name='record_update'),
    url(r'^record/(?P<pk>\d+)/delete/$', MedicalRecordDelete.as_view(), name='record_delete'),
)
