from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

WSGI_APPLICATION = 'horsys.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'horsys',
        'HOST': 'localhost',
        'PORT': '',
        'USER': '',
        'PASSWORD': ''
    },
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'horsys.db'),
    }
}

INSTALLED_APPS += (
    'core',
    'horses',
    'schedule',
    'customers',
    'dashboard',

    'registration',
    'registration.contrib.notification',
    'bootstrap3_datetime',
    'debug_toolbar',
    'autofixture',
    'dev',
)

REGISTRATION_SUPPLEMENT_CLASS = None
ACCOUNT_ACTIVATION_DAYS       = 7
