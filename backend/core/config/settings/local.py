from .main import *
# STATIC_URL = '/static/'
DEBUG = True
INSTALLED_APPS.extend(['debug_toolbar',])
MIDDLEWARE.extend(['debug_toolbar.middleware.DebugToolbarMiddleware',])
INTERNAL_IPS = [
    '127.0.0.1',
]
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,  # Насильно включить
}
ALLOWED_HOSTS = ['*']