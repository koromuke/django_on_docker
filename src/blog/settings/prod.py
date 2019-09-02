import os
import random
import string

import dj_database_url
import django_cache_url

from .base import *

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = os.getenv('DJANGO_DEBUG', 'off') == 'on'

# SECRET_KEY = 'nh2qv&*4mtag^-vg+b4+g+u=_!*u&6%$$mk_o1$!=rc1^hb41s'
# DJANGO_SECRET_KEY *should* be specified in the environment. If it's not, generate an ephemeral key.
if 'DJANGO_SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
else:
    # Use if/else rather than a default value to avoid calculating this if we don't need it
    print("WARNING: DJANGO_SECRET_KEY not found in os.environ. Generating ephemeral SECRET_KEY.")
    SECRET_KEY = ''.join([random.SystemRandom().choice(string.printable) for i in range(50)])


# ALLOWED_HOSTS = ['localhost']
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '*').split(';')

BASE_URL = 'http://localhost:8000'


# To send email from the server, we recommend django_sendmail_backend
# Or specify your own email backend such as an SMTP server.
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-backend
# EMAIL_BACKEND = 'django_sendmail_backend.backends.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Default email address used to send messages from the website.
DEFAULT_FROM_EMAIL = 'base <info@localhost>'

# A list of people who get error notifications.
ADMINS = [
    ('Administrator', 'admin@localhost'),
]

# A list in the same format as ADMINS that specifies who should get broken link
# (404) notifications when BrokenLinkEmailsMiddleware is enabled.
MANAGERS = ADMINS

# Email address used to send error messages to ADMINS.
SERVER_EMAIL = DEFAULT_FROM_EMAIL

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'HOST': 'localhost',
#        'NAME': 'blog',
#        'USER': 'blog',
#        'PASSWORD': '',
#        # If using SSL to connect to a cloud mysql database, spedify the CA as so.
#        'OPTIONS': { 'ssl': { 'ca': '/path/to/certificate-authority.pem' } },
#    }
#}

# Use template caching to speed up wagtail admin and front-end.
# Requires reloading web server to pick up template changes.
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#                 'wagtail.contrib.settings.context_processors.settings',
#             ],
#             'loaders': [
#                 ('django.template.loaders.cached.Loader', [
#                     'django.template.loaders.filesystem.Loader',
#                     'django.template.loaders.app_directories.Loader',
#                 ]),
#             ],
#         },
#     },
# ]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache'),
        'KEY_PREFIX': 'coderedcms',
        'TIMEOUT': 14400, # in seconds
    }
}

try:
    from .local_settings import *
except ImportError:
    pass


WAGTAIL_CACHE = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}
