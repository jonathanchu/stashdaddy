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
ADMINS = (
    ('Jonathan Chu', 'jc@3atmospheres.com'),
)


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
    # django-suit needs to be before django.contrib.admin
    'suit',

    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # third-party packages
    'compressor',
    # 'djcelery',
    'django_forms_bootstrap',
    'gunicorn',
    # 'kombu.transport.django',
    'raven.contrib.django.raven_compat',
    'south',
    'taggit',
    # 'tastypie',

    # stashdaddy apps
    # 'accounts',
    'bookmarks',
    'core',
]

# LOGGING
#
# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# AUTH STUFF
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = '/'
# AUTH_USER_MODEL = 'accounts.CustomUser'
# AUTH_PROFILE_MODULE = 'accounts.UserProfile'
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

# DJANGO-SUIT CONFIG
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Stashdaddy Admin',
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # Parameter also accepts url name
    # 'SEARCH_URL': 'admin:auth_user_changelist',
    # Set to empty string if you want to hide search from menu
    # 'SEARCH_URL': ''

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    'MENU_EXCLUDE': ('auth.group',),
    # 'MENU': (
    #     'sites',
    #     {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
    #     {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    # ),

    # misc
    # 'LIST_PER_PAGE': 15
}
