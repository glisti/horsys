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
    url(r'^wiki/', get_wiki_pattern()),
    url(r'^customers/', include('customers.urls')),
    url('^registration/', include('registration.urls')),
)

# django.contrib.auth
from django.contrib.auth import views as auth_views
urlpatterns += patterns('',
    url(r'^login/$', auth_views.login,
        {'template_name': 'registration/login.html'},
        name='auth_login'),
    url(r'^logout/$', auth_views.logout,
        {'template_name': 'registration/logout.html'},
        name='auth_logout'),
    url(r'^password/change/$', auth_views.password_change,
        name='password_change'),
    url(r'^password/change/done/$', auth_views.password_change_done,
        name='password_change_done'),
    url(r'^password/reset/$', auth_views.password_reset,
        name='password_reset'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^password/reset/complete/$', auth_views.password_reset_complete,
        name='password_reset_complete'),
    url(r'^password/reset/done/$', auth_views.password_reset_done,
        name='password_reset_done'),
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
