from .base import *


DEBUG = TEMPLATE_DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
GAUGES_SITE_ID = False
COMPRESS_ENABLED = False

# SENTRY
RAVEN_CONFIG = {
    'dsn': 'http://9f4ba557c12f4e409fe7da2098c0db26:4807ba1d40d240b184cc371719bf9bf6@0.0.0.0:9000/2',
}

try:
    import debug_toolbar
except ImportError:
    pass
else:
    INSTALLED_APPS.append('debug_toolbar')
    INSTALLED_APPS.append('cache_panel')
    INTERNAL_IPS = ('127.0.0.1',)
    MIDDLEWARE_CLASSES.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'cache_panel.panel.CacheDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
        'debug_toolbar.panels.profiling.ProfilingDebugPanel',
    )

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
