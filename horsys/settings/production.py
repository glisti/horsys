from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

WSGI_APPLICATION = 'horsys.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'horsysdb',
        'HOST': 'localhost',
        'PORT': '',
        'USER': 'postgres',
        'PASSWORD': 'Ir5Lmc67m2'
    }
}

INSTALLED_APPS += (
    'horses',
    'schedule',
    'customers',
    'core',
    'registration',
    'registration.contrib.notification',
)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
STATIC_ROOT = ''
STATIC_URL = '/static/'

ROOT_PATH = os.path.join(os.path.dirname(__file__), '..')  # up one level from settings.py
STATICFILES_DIRS = (
    os.path.abspath(os.path.join(ROOT_PATH, 'static')), # static is on root level
)

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#)
