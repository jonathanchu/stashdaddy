from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    """
    Extends the ``User`` model to allow for additional user attributes
    """
    user = models.OneToOneField(User, related_name='profile')
    first_name = models.CharField(blank=True, null=True, max_length=255)
    last_name = models.CharField(blank=True, null=True, max_length=255)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __unicode__(self):
        if self.user.get_full_name():
            return unicode(self.user.get_full_name())
        else:
            return unicode(self.user.username)
