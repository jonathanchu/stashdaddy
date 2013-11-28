from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView

from django.contrib import admin
from bookmarks.views import BookmarkList, BookmarkCreate, MyBookmarks, \
    BookmarkEdit

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$',                         TemplateView.as_view(template_name='home.html'), name='home'),
    # url(r'^(?P<username>[\-\.\w]+)/$', BookmarkList.as_view(),   name='bookmarks_list'),
    url(r'^new/$',                     BookmarkCreate.as_view(), name='bookmark_create'),
    url(r'^mine/$',                    MyBookmarks.as_view(),     name='bookmarks_list_mine'),
    url(r'^(?P<pk>\d+)/edit/$',        BookmarkEdit.as_view(),        name='bookmark_edit'),
    # (r'^api/', include(bookmark_resource.urls)),

    # accounts
    (r'^accounts/', include('registration.backends.default.urls')),

    # temp convenience auth urls
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    # url(r'^login/$',                   Login.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),

    # admin
    url(r'^admin/', include(admin.site.urls)),
)
