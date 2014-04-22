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
    }
    # 'default_lite': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'horsys.db'),
    # }
}

INSTALLED_APPS += (
    'horses',
    'schedule',
    'debug_toolbar',
    'autofixture',
    'dev',
    'core',
    'registration',
)

REGISTRATION_SUPPLEMENT_CLASS = None
ACCOUNT_ACTIVATION_DAYS       = 7

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'glisti14@gmail.com'
EMAIL_HOST_PASSWORD = 'tamu2014'