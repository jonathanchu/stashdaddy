from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

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
