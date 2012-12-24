from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from settings import DEBUG, MEDIA_ROOT, STATIC_ROOT

urlpatterns = patterns('',
    # home
    url(r'^$', direct_to_template, {'template': 'home.html'}, name='home'),

    # accounts
    (r'^accounts/', include('registration.backends.default.urls')),

    # profile
    url(r'^accounts/profile/', 'accounts.views.account', name='profile'),

    # admin
    url(r'^admin/', include(admin.site.urls)),
)

if DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': MEDIA_ROOT, 'show_indexes': True, }),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': STATIC_ROOT, 'show_indexes': True, }),
    )
