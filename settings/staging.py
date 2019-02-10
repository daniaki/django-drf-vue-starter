# settings/local.py
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ADMIN_ENABLED = DEBUG

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]

# Logging
# Add/Modify existing loggers using the format below

LOGGING_LEVEL = 'INFO'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] %(asctime)s %(module)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'django': {
            'level': LOGGING_LEVEL,
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'verbose'
        },

    },
    'loggers': {
        'django': {
            'handlers': ['django'],
            'level': LOGGING_LEVEL,
            'propagate': True
        },
    },
}
