from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    """
    Basic published manager.
    """
    def published(self, *args, **kwargs):
        qs = self.get_query_set().filter(*args, **kwargs)
        return qs.filter(pub_date__lte==timezone.now())
