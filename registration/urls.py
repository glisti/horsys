# coding=utf-8
"""
URLconf for django-inspectional-registration
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
from registration.compat import url
from registration.compat import patterns

from registration.views import RegistrationView
from registration.views import RegistrationClosedView
from registration.views import RegistrationCompleteView
from registration.views import ActivationView
from registration.views import ActivationCompleteView

urlpatterns = patterns('',
    url(r'^activate/complete/$', ActivationCompleteView.as_view(),
        name='registration_activation_complete'),
    url(r'^activate/(?P<activation_key>\w+)/$', ActivationView.as_view(),
        name='registration_activate'),
    url(r'^register/$', RegistrationView.as_view(),
        name='registration_register'),
    url(r'^register/closed/$', RegistrationClosedView.as_view(),
        name='registration_disallowed'),
    url(r'^register/complete/$', RegistrationCompleteView.as_view(),
        name='registration_complete'),
)
