import os
import sys

from postgresify import postgresify
from unipath import Path

# BASIC SETUP
PROJECT_ROOT = Path(__file__).ancestor(2)
sys.path.insert(0, PROJECT_ROOT)
DEBUG = TEMPLATE_DEBUG = False
ROOT_URLCONF = 'stashdaddy.urls'
SECRET_KEY = os.environ['SECRET_KEY']
SITE_ID = 1
TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# DATABASES
DATABASES = postgresify()

# MEDIA, ASSETS, ETC.
MEDIA_ROOT = PROJECT_ROOT.child('media')
MEDIA_URL = '/media/'
STATIC_ROOT = PROJECT_ROOT.child('static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [PROJECT_ROOT.child('assets')]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# TEMPLATES
TEMPLATE_DIRS = [PROJECT_ROOT.child('templates')]

# MIDDLEWARE
MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# TEMPLATE CONTEXT PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    # "django.core.context_processors.static",
]

# APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # third-party packages
    'compressor',
    'djcelery',
    'django_forms_bootstrap',
    'gunicorn',
    'kombu.transport.django',
    'south',
    'taggit',
    # 'tastypie',

    # stashdaddy apps
    'accounts',
    'bookmarks',
    'core',
]

# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# AUTH STUFF
ACCOUNT_ACTIVATION_DAYS = 7
AUTH_USER_MODEL = 'accounts.CustomUser'
AUTH_PROFILE_MODULE = 'accounts.UserProfile'
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
POCKET_API_KEY = os.environ['POCKET_API_KEY']

# ANALYTICS
GAUGES_SITE_ID = os.environ['GAUGES_SITE_ID']

# TASK QUEUE
BROKER_BACKEND = 'django'

# COMPRESSOR SETTINGS
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_ROOT = PROJECT_ROOT.child('assets')
COMPRESS_PRECOMPILERS = (
   ('text/less', 'lessc {infile} {outfile}'),
)
COMPRESS_CSS_FILTERS = [
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter'
]
