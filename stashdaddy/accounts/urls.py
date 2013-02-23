from django.conf.urls.defaults import pattersn, include, url
from .views import *


urlpatterns = patterns(
    '',
    url(r'^dashboard/$',           views.dashboard,            name='accounts_dashboard'),
    url(r'^login/$',               views.login,                name='accounts_login'),
    url(r'^logout/$',              views.logout,               name='accounts_logout'),
    url(r'^register/$',            views.register,             name='accounts_register'),
    url(r'^password/change/$',     views.password_change,      name='accounts_password_change'),
    url(r'^password/done/$',       views.password_change_done, name='accounts_password_done'),
    url(r'^password/reset/$',      views.password_reset,       name='accounts_password_reset'),
    url(r'^password/reset/done/$', views.password_reset_done,  name='accounts_password_reset_done'),
)
