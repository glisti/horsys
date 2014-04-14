from django.conf.urls import patterns, include, url
from customers.views import *
urlpatterns = patterns('',
    url(r'^$', BoarderList.as_view(), name='boarder_list'),
	url(r'^add/$', BoarderCreate.as_view(), name='boarder_create'),
	url(r'^(?P<pk>\d+)/$', BoarderDetail.as_view(), name='boarder_detail'),
)