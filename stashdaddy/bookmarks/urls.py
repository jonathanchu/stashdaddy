from django.conf.urls.defaults import patterns, include, url
from . import views


urlpatterns = patterns(
    '',
    url(r'^$',                  views.BookmarkList.as_view(),   name='bookmarks_list'),
    url(r'^new/$',              views.BookmarkCreate.as_view(), name='bookmark_create'),
    url(r'^mine/$',             views.MyListings.as_view(),     name='bookmarks_list_mine'),
    url(r'^(?P<pk>\d+)/$',      views.BookmarkDetail.as_view(), name='bookmark_edit'),
    url(r'^(?P<pk>\d+)/edit/$', views.BookmarkEdit.as_view(),   name='bookmark_edit'),
)
