from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # home
    url(r'^$', direct_to_template, {'template': 'home.html'}, name='home'),

    # accounts and registration
    (r'^accounts/', include('registration.backends.default.urls')),

    # admin
    url(r'^admin/', include(admin.site.urls)),
)
