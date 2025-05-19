from .main import *

DEBUG = True
INSTALLED_APPS.extend(['debug_toolbar',])
MIDDLEWARE.extend(['debug_toolbar.middleware.DebugToolbarMiddleware',])
# INTERNAL_IPS = [
#     '127.0.0.1',
# ]
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,  # Насильно включить
}
ALLOWED_HOSTS = ['*']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': env('POSTGRES_NAME'),
#         'USER': env('POSTGRES_USER'),
#         'PASSWORD': env('POSTGRES_PASSWORD'),
#         'HOST': 'localhost',
#         'PORT': '5433',
#     }
# }


# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://localhost:6379/1",  
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }
# CELERY_BROKER_URL = 'redis://redis:6379/0'
# CELERY_RESULT_BACKEND = 'redis://redis:6379/0'