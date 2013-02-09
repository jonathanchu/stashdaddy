from tastypie.resources import ModelResource

from .models import Bookmark


class BookmarkResource(ModelResource):
    class Meta:
        queryset = Bookmark.objects.all()
        resource_name = 'bookmark_resource'
