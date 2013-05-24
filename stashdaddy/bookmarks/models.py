from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

# from settings.base import AUTH_USER_MODEL


class Bookmark(models.Model):
    """
    A bookmark is a unique URL that is associated with a user
    """
    url = models.URLField()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)
    private = models.BooleanField(default=False)
    # user = models.ForeignKey(AUTH_USER_MODEL, related_name='bookmarks')
    user = models.ForeignKey(User, related_name='bookmarks')
    added_at = models.DateTimeField(auto_now=True, editable=False)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('bookmark')
        verbose_name_plural = _('bookmarks')
        ordering = ('-added_at',)
        get_latest_by = "added_at"

    def __unicode__(self):
        return self.title
