from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from customers.views import *#BoardersList, BoardersCreate, BoardersDetail \
                            #,BoardersUpdate, BoardersDelete, OwnersList, OwnersCreate \
                            #,BoardersDetail, OwnersUpdate, OwnersDelete, OwnersDetail \
                            #,ContactInfoCreate, ContactInfoList,OwnerContactInfoCreate, OwnerContactInfoList \
                            #,OwnerContactInfoDelete, OwnerContactInfoUpdate
urlpatterns = patterns('',
    #Boarder
    url(r'^$', TemplateView.as_view(template_name='customers\customer_list.html'), name='customer_list'),
    url(r'^boarders/$', BoardersList.as_view(), name='boarder_list'),
    url(r'^boarders/add/$', BoardersCreate.as_view(), name='boarder_create'),
    url(r'^boarders/(?P<pk>\d+)/$', BoardersDetail.as_view(), name='boarder_detail'),
    url(r'^boarders/(?P<pk>\d+)/update/$', BoardersUpdate.as_view(), name='boarders_update'),
    url(r'^boarders/(?P<pk>\d+)/delete/$', BoardersDelete.as_view(), name='boarders_delete'),
    #Owner
    url(r'^owners/$', OwnersList.as_view(), name='owner_list'),
    url(r'^owners/add/$', OwnersCreate.as_view(), name='owner_create'),
    url(r'^owners/(?P<pk>\d+)/$', OwnersDetail.as_view(), name='owner_detail'),
    url(r'^owners/(?P<pk>\d+)/update/$', OwnersUpdate.as_view(), name='owner_update'),
    url(r'^owners/(?P<pk>\d+)/delete/$', OwnersDelete.as_view(), name='owner_delete'),
    #Contact Info
    url(r'^contact/add/$', ContactInfoCreate.as_view(), name='contactinfo_create'),
    url(r'^contact/$', ContactInfoList.as_view(), name='contact_list'),
    url(r'^contact/(?P<pk>\d+)/$', ContactInfoList.as_view(), name='contactinfo_detail'),
    url(r'^contact/(?P<pk>\d+)/update/$', ContactInfoUpdate.as_view(), name='contactinfo_update'),
    url(r'^contact/(?P<pk>\d+)/delete/$', ContactInfoDelete.as_view(), name='contactinfo_delete'),

    #Contact Info
    url(r'^owners/contact/add/$', OwnerContactInfoCreate.as_view(), name='ownercontactinfo_create'),
    url(r'^owners/contact/$', OwnerContactInfoList.as_view(), name='ownercontact_list'),
    url(r'^owners/contact/(?P<pk>\d+)/$', OwnerContactInfoList.as_view(), name='ownercontactinfo_detail'),
    url(r'^owners/contact/(?P<pk>\d+)/update/$', OwnerContactInfoUpdate.as_view(), name='ownercontactinfo_update'),
    url(r'^owners/contact/(?P<pk>\d+)/delete/$', OwnerContactInfoDelete.as_view(), name='ownercontactinfo_delete'),

)