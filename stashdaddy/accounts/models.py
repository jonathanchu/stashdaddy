from __future__ import unicode_literals
import warnings

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    """
    A thin wrapper around the default BaseUserManager
    """
    def create_user(self, email=None, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = UserManager.normalize_email(email)
        user = self.model(email=email,
                          is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, date_joined=now)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        u = self.create_user(email, password)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), max_length=254)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __unicode__(self):
        return self.email

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.username)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def get_profile(self):
        """
        Returns site-specific profile for this user. Raises
        SiteProfileNotAvailable if this site does not allow profiles.
        """
        warnings.warn("The use of AUTH_PROFILE_MODULE to define user profiles has been deprecated.",
            DeprecationWarning, stacklevel=2)
        if not hasattr(self, '_profile_cache'):
            from django.conf import settings
            if not getattr(settings, 'AUTH_PROFILE_MODULE', False):
                raise SiteProfileNotAvailable(
                    'You need to set AUTH_PROFILE_MODULE in your project '
                    'settings')
            try:
                app_label, model_name = settings.AUTH_PROFILE_MODULE.split('.')
            except ValueError:
                raise SiteProfileNotAvailable(
                    'app_label and model_name should be separated by a dot in '
                    'the AUTH_PROFILE_MODULE setting')
            try:
                model = models.get_model(app_label, model_name)
                if model is None:
                    raise SiteProfileNotAvailable(
                        'Unable to load the profile model, check '
                        'AUTH_PROFILE_MODULE in your project settings')
                self._profile_cache = model._default_manager.using(
                                   self._state.db).get(user__id__exact=self.id)
                self._profile_cache.user = self
            except (ImportError, ImproperlyConfigured):
                raise SiteProfileNotAvailable
        return self._profile_cache


# class UserProfile(models.Model):
#     """
#     Extends the ``User`` model to allow for additional user attributes
#     """
#     user = models.OneToOneField(User, related_name='profile')
#     first_name = models.CharField(blank=True, null=True, max_length=255)
#     last_name = models.CharField(blank=True, null=True, max_length=255)
#     email = models.EmailField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now=True, editable=False)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name = 'profile'
#         verbose_name_plural = 'profiles'

#     def __unicode__(self):
#         if self.user.get_full_name():
#             return unicode(self.user.get_full_name())
#         else:
#             return unicode(self.user.username)

# def create_profile(sender, instance, **kwargs):
#     """
#     Create a user profile object each time a User is created.
#     """
#     UserProfile.objects.get_or_create(user=instance)

# post_save.connect(create_profile, sender=User)
