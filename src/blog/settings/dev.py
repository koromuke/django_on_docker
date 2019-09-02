from .base import *

# DEBUG = True
# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'nh2qv&*4mtag^-vg+b4+g+u=_!*u&6%$$mk_o1$!=rc1^hb41s'

# SECRET_KEY = '%wil9tbxj0+#ci7b!5oz8(j_$&r^9*ttyups0=2qwv#rn(fns8'

# ALLOWED_HOSTS = ['*']

BASE_URL = 'http://localhost:8000'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAIL_CACHE = False

try:
    from .local_settings import *
except ImportError:
    pass
