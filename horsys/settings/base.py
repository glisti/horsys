"""
Django settings for horsys project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR    = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o_asryzz+d8+ut7aukg1=&&8wrmi8lb-ru-70k1ln#5i0yexxq'

ADMINS = (('horsys staff','horsys.staff@gmail.com'),)

ALLOWED_HOSTS = ['*']

SITE_ID = 1

# User URLs
LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'

LOGOUT_URL = '/logout/'

# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # django 1.6.2
    'django.contrib.humanize',
    'south',
    'stronghold',
    'crispy_forms',
    'django_notify',
    'mptt',
    'sekizai',
    'sorl.thumbnail',
    'wiki',
    'wiki.plugins.attachments',
    'wiki.plugins.notifications',
    'wiki.plugins.images',
    'wiki.plugins.macros',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'stronghold.middleware.LoginRequiredMiddleware',
)

ROOT_URLCONF = 'horsys.urls'

WSGI_APPLICATION = 'horsys.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#DATABASES = {}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE     = 'UTC'

USE_I18N      = True

USE_L10N      = True

USE_TZ        = True

# SMTP

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'horsys.staff@gmail.com'
EMAIL_HOST_PASSWORD = 'horsysstaff'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL    = '/static/'

TEMPLATE_CONTEXT_PROCESSORS = (

"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.request",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages",
"sekizai.context_processors.sekizai",

)

TEMPLATE_DIRS = [os.path.join(PROJECT_DIR, 'templates')]

MEDIA_URL     = '/media/'

MEDIA_ROOT    = os.path.join(PROJECT_DIR,'media')

# 3rd Party Settings

STRONGHOLD_DEFAULTS = True

STRONGHOLD_PUBLIC_NAMED_URLS = ('auth_login','auth_logout','password_reset',
                                'password_reset_confirm','password_reset_complete',
                                'password_reset_done','registration_activation_complete',
                                'registration_activate','registration_register',
                                'registration_disallowed','registration_complete')

REGISTRATION_SUPPLEMENT_CLASS = None
ACCOUNT_ACTIVATION_DAYS       = 7

CRISPY_TEMPLATE_PACK = 'bootstrap3'

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}
