from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Link(models.Model):
    """Model for keeping info about url."""
    user = models.ForeignKey(User, verbose_name=_('author'), on_delete=models.CASCADE, related_name='links')
    url = models.URLField(verbose_name=_('url'), max_length=255)
    status_code = models.PositiveSmallIntegerField(verbose_name=_('status code'), default=0)

    @property
    def color(self) -> str:
        status_starts_with = str(self.status_code)[0]
        color = 'default'

        match status_starts_with:
            case 1 | 2 | 3:
                color = 'green'
            case 4 | 5:
                color = 'red'

        return color

    color.fget.short_description = _('color')

    def __str__(self):
        return self.url

    class Meta:
        ordering = ('-id', 'url')
        verbose_name = _('Link')
        verbose_name_plural = _('Links')
