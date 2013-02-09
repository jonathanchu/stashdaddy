from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
from bookmarks.views import BookmarkList, BookmarkCreate, MyBookmarks, BookmarkEdit
from bookmarks.api import BookmarkResource


bookmark_resource = BookmarkResource()
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',                         direct_to_template, {'template': 'home.html'}, name='home'),
    # url(r'^(?P<username>[\-\.\w]+)/$', BookmarkList.as_view(),   name='bookmarks_list'),
    url(r'^new/$',                     BookmarkCreate.as_view(), name='bookmark_create'),
    url(r'^mine/$',                    MyBookmarks.as_view(),     name='bookmarks_list_mine'),
    url(r'^(?P<pk>\d+)/edit/$',        BookmarkEdit.as_view(),        name='bookmark_edit'),
    (r'^api/', include(bookmark_resource.urls)),

    # accounts
    (r'^accounts/',                    include('registration.backends.default.urls')),

    # profile
    url(r'^accounts/profile/', 'accounts.views.account', name='profile'),

    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
