from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^horses/', include('horses.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^schedule/', include('schedule.urls')),
)
