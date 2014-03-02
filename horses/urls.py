from django.conf.urls import patterns, include, url
from horses.views import HorseList, HorseCreate, HorseDetail, \
                         HorseUpdate, HorseDelete
urlpatterns = patterns('',
    url(r'^$', HorseList.as_view(), name='horse_list'),
    url(r'^add/$', HorseCreate.as_view(), name='horse_create'),
    url(r'^(?P<pk>\d+)/$', HorseDetail.as_view(), name='horse_detail'),
    url(r'^(?P<pk>\d+)/update/$', HorseUpdate.as_view(), name='horse_update'),
    url(r'^(?P<pk>\d+)/delete/$', HorseDelete.as_view(), name='horse_delete'),
)
