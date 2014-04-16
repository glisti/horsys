from django.conf.urls import patterns, include, url
from schedule.views import (ShiftList, ShiftCreate,
                            ShiftDetail, ShiftDelete, ScheduleHome,
                            ClockList, ClockCreate, ClockDetail, ClockDelete)

urlpatterns = patterns('',
    url(r'^shifts/$', ShiftList.as_view(), name='shift_list'),
    url(r'^shifts/add/$', ShiftCreate.as_view(), name='shift_create'),
    url(r'^shifts/(?P<pk>\d+)/$', ShiftDetail.as_view(), name='shift_detail'),
    # url(r'^shift/(?P<pk>\d+)/update/$', ShiftAMUpdate.as_view(), name='shiftAM_update'),
    url(r'^shifts/(?P<pk>\d+)/delete/$', ShiftDelete.as_view(), name='shift_delete'),
    url(r'^$', ScheduleHome.as_view(), name='schedule_home'),
    url(r'^clock/$', ClockList.as_view(), name='clock_list'),
    url(r'^clock/add/$', ClockCreate.as_view(), name='clock_create'),
    url(r'^clock/(?P<pk>\d+)/$', ClockDetail.as_view(), name='clock_detail'),
    # url(r'^shift/(?P<pk>\d+)/update/$', ShiftAMUpdate.as_view(), name='shiftAM_update'),
    url(r'^clock/(?P<pk>\d+)/delete/$', ClockDelete.as_view(), name='clock_delete'),
)