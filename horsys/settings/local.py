from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

WSGI_APPLICATION = 'horsys.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'horsys.db'),
    }
}

INSTALLED_APPS += (
    'horses',
    'schedule',
	'customers',
    'debug_toolbar',
    'autofixture',
    'dev',
    'core',
)