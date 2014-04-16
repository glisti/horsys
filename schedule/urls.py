from django.conf.urls import patterns, include, url
from schedule.views import (ShiftList, ShiftCreate, ShiftUpdate,
                            ShiftDetail, ShiftDelete)

urlpatterns = patterns('',
    url(r'^shifts/$', ShiftList.as_view(), name='shift_list'),
    url(r'^shift/(?P<pk>\d+)/$', ShiftDetail.as_view(), name='shift_detail'),
    url(r'^shift/(?P<time>[AP]M)/add/$', ShiftCreate.as_view(), name='shift_create'),
    url(r'^shift/(?P<time>[AP]M)/(?P<pk>\d+)/update/$', ShiftUpdate.as_view(), name='shift_update'),
    url(r'^shift/(?P<pk>\d+)/delete/$', ShiftDelete.as_view(), name='shift_delete'),
)