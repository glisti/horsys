from django.conf.urls import patterns, include, url
from schedule.views import LogList, LogCreate, LogDetail, \
                         LogUpdate, LogDelete, ShiftAMList, ShiftAMCreate, ShiftAMDetail, \
                         ShiftAMUpdate, ShiftAMDelete, ShiftPMCreate, ShiftPMDetail, ShiftPMUpdate, ShiftPMDelete
urlpatterns = patterns('',
    url(r'^$', LogList.as_view(), name='log_list'),
    url(r'^add/$', LogCreate.as_view(), name='log_create'),
    url(r'^(?P<pk>\d+)/$', LogDetail.as_view(), name='log_detail'),
    url(r'^(?P<pk>\d+)/update/$', LogUpdate.as_view(), name='log_update'),
    url(r'^(?P<pk>\d+)/delete/$', LogDelete.as_view(), name='log_delete'),
    url(r'^shiftAM/$', ShiftAMList.as_view(), name='shiftAM_list'),
    url(r'^shiftAM/add/$', ShiftAMCreate.as_view(), name='shiftAM_create'),
    url(r'^shiftAM/(?P<pk>\d+)/$', ShiftAMDetail.as_view(), name='shiftAM_detail'),
    url(r'^shiftAM/(?P<pk>\d+)/update/$', ShiftAMUpdate.as_view(), name='shiftAM_update'),
    url(r'^shiftAM/(?P<pk>\d+)/delete/$', ShiftAMDelete.as_view(), name='shiftAM_delete'),
    url(r'^shiftPM/add/$', ShiftPMCreate.as_view(), name='shiftPM_create'),
    url(r'^shiftPM/(?P<pk>\d+)/$', ShiftPMDetail.as_view(), name='shiftPM_detail'),
    url(r'^shiftPM/(?P<pk>\d+)/update/$', ShiftPMUpdate.as_view(), name='shiftPM_update'),
    url(r'^shiftPM/(?P<pk>\d+)/delete/$', ShiftPMDelete.as_view(), name='shiftPM_delete'),
)