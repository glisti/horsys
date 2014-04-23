from django.conf.urls import patterns, include, url
from schedule.views import (ShiftList, ShiftAMCreate, ShiftPMCreate,
                            ShiftAMUpdate, ShiftPMUpdate, ShiftDetail, ShiftDelete,
                            ScheduleHome) 

urlpatterns = patterns('',
    url(r'^shifts/$', ShiftList.as_view(), name='shift_list'),
    url(r'^shift/(?P<pk>\d+)/$', ShiftDetail.as_view(), name='shift_detail'),
    url(r'^shift/AM/add/$', ShiftAMCreate.as_view(), name='shiftam_create'),
    url(r'^shift/PM/add/$', ShiftPMCreate.as_view(), name='shiftpm_create'),
    url(r'^shift/AM/(?P<pk>\d+)/update/$', ShiftAMUpdate.as_view(), name='shiftam_update'),
    url(r'^shift/PM/(?P<pk>\d+)/update/$', ShiftPMUpdate.as_view(), name='shiftpm_update'),
    url(r'^shift/(?P<pk>\d+)/delete/$', ShiftDelete.as_view(), name='shift_delete'),
    url(r'^$', ScheduleHome.as_view(), name='schedule_home'), )
