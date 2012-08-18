# Django settings for stashdaddy project.

import os
import sys
import dj_database_url

## DEBUGGING
# ---------------------------------------------------------------------------

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Jonathan Chu', 'jonathan.chu@me.com'),
)

MANAGERS = ADMINS

## DATABASE
# ---------------------------------------------------------------------------

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

## GLOBAL PATHS
# ---------------------------------------------------------------------------

join_path = lambda p1,p2: os.path.abspath(os.path.join(p1,p2))

PROJECT = os.path.abspath(os.path.dirname(__file__))
APPS_ROOT = join_path(PROJECT, 'apps')
TEMPLATE_DIRS = (join_path(PROJECT, 'templates'),)

sys.path.insert(0, APPS_ROOT)

## LOCALE
# ---------------------------------------------------------------------------

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
USE_TZ = True

SITE_ID = 1
USE_I18N = True
USE_L10N = True

## STATIC MEDIA
# ---------------------------------------------------------------------------

MEDIA_ROOT = join_path(PROJECT, 'media')
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    join_path(PROJECT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

## USERS + AUTHENTICATION
# ---------------------------------------------------------------------------

SECRET_KEY = 'm0l%vh6%zg$ngj%st_vbt&amp;u1o$%v%!#xq=#+7_+9ml)aaint4)'

# ## INTERNALS
# ---------------------------------------------------------------------------

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
)

## URL RESOLVING
# ---------------------------------------------------------------------------

ROOT_URLCONF = 'stashdaddy.urls'


WSGI_APPLICATION = 'stashdaddy.wsgi.application'

## APPLICATIONS
# ---------------------------------------------------------------------------

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # third-party packages,
    'gunicorn',
    'registration',
    'south',

    # stashdaddy apps

)

## EXTERNAL RESOURCE AUTHENTICATION
# ---------------------------------------------------------------------------

TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''

## ANALYTICS
# ---------------------------------------------------------------------------

GAUGES_SITE_ID = '502f8335f5a1f5622a000002'

## EMAIL
# ---------------------------------------------------------------------------


## LOGGING
# ---------------------------------------------------------------------------

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

## ENVIRONMENTS
# ---------------------------------------------------------------------------

try:
    from local_settings import *
except ImportError:
    pass
