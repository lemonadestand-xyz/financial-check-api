from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "sherlocked")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", True)

# Allowed hosts who can connect with Django app
ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
        "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "switchboard_demo",
        "USER": "postgres",
        "PASSWORD": "switchboard-123!",
        "HOST": "35.222.175.187"
    }
}

# time zone settings
TIME_ZONE = 'Asia/Calcutta'

USE_TZ = True

# celery and broker configurations
BROKER_USER = os.environ.get("BROKER_USER", "plaidrabbitadmin")
BROKER_PASSWORD = os.environ.get("BROKER_PASSWORD", "password")
BROKER_HOST = os.environ.get("BROKER_HOST", "0.0.0.0")
BROKER_PORT = os.environ.get("BROKER_PORT", "5672")
BROKER_VHOST = os.environ.get("BROKER_VHOST", "/")

CELERY_BROKER_URL = f"amqp://{BROKER_USER}:{BROKER_PASSWORD}@{BROKER_HOST}:{BROKER_PORT}/{BROKER_VHOST}"

# Don't use pickle as serializer, json is much safer
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ['application/json']

CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = os.environ.get("TIME_ZONE", "Asia/Calcutta")

# Plaid configurations
PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID', '5f0cf3f4584f980012e75985')
PLAID_SECRET = os.getenv('PLAID_SECRET', 'c954eb87be5645f10f2f9e4d4ea9ff')
PLAID_PUBLIC_KEY = os.getenv('PLAID_PUBLIC_KEY', '86ffca7cb26f7931d479bac2594351')
PLAID_ENV = os.getenv('PLAID_ENV', 'sandbox')
PLAID_COUNTRY_CODES = os.getenv('PLAID_COUNTRY_CODES', 'US,CA,GB,FR,ES')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = "mjrulesamrat@gmail.com"

# API CORS Allow all for now
CORS_ORIGIN_ALLOW_ALL = True

# DJOSER config
DJOSER = {
    'SEND_ACTIVATION_EMAIL': False,
}
