from .base import *


DEBUG = True

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = ["127.0.0.1"]


# Email Settings
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
