import os

from .base import *  # noqa
from .base import env


ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']


INSTALLED_APPS = ['whitenoise.runserver_nostatic'] + INSTALLED_APPS  # noqa F405


INSTALLED_APPS += ['debug_toolbar']  # noqa F405
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']  # noqa F405
DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': ['debug_toolbar.panels.redirects.RedirectsPanel'],
    'SHOW_TEMPLATE_CONTEXT': True,
}
INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']
if env('USE_DOCKER') == 'yes':
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += ['.'.join(ip.split('.')[:-1] + ['1']) for ip in ips]

INSTALLED_APPS += ['django_extensions']  # noqa F405

CELERY_TASK_EAGER_PROPAGATES = True

# Taken from constance
# TODO: If dynamic constance takes place in project, put this lines there

BIOMETRY_HOME_PAGE = os.getenv('BIOMETRY_HOME_PAGE', 'https://llconveyer.kz')

FFIN_BIOMETRY_HOST = os.getenv(
    'FFIN_BIOMETRY_HOST',
    'https://dev-biometry.trafficwave.kz',
)

REDIS_URL = os.getenv('REDIS_URL', 'redis://redis:6379/0')

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'apps.notifications.channel_layers'
                   '.RedisChannelLayerGroupPersistence',
        'CONFIG': {
            'hosts': [REDIS_URL],
        },
    },
}
# Отправлять SMS
SEND_SMS = False
