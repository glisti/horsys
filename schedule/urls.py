from django.conf.urls import patterns, include, url
from schedule.views import (ShiftList, ShiftAMCreate, ShiftPMCreate,
                            ShiftDetail, ShiftDelete)

urlpatterns = patterns('',
    url(r'^shifts/$', ShiftList.as_view(), name='shift_list'),
    url(r'^shift/AM/add/$', ShiftAMCreate.as_view(), name='shiftAM_create'),
    url(r'^shift/PM/add/$', ShiftAMCreate.as_view(), name='shiftPM_create'),
    url(r'^shift/(?P<pk>\d+)/$', ShiftDetail.as_view(), name='shift_detail'),
    # url(r'^shift/(?P<pk>\d+)/update/$', ShiftAMUpdate.as_view(), name='shiftAM_update'),
    url(r'^shift/(?P<pk>\d+)/delete/$', ShiftDelete.as_view(), name='shiftAM_delete'),
)