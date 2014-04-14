from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from wiki.urls import get_pattern as get_wiki_pattern
from django_notify.urls import get_pattern as get_notify_pattern

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='landing.html'), name='landing'),
    url(r'^horses/', include('horses.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^schedule/', include('schedule.urls')),
    url(r'^notify/', get_notify_pattern()),
    url(r'^wiki/', get_wiki_pattern())
    url(r'^customers/', include('customers.urls')),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),

)
