from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """Model for keeping info about user."""

    class Meta:
        ordering = ('-date_joined',)
        verbose_name = _('user')
        verbose_name_plural = _('users')
