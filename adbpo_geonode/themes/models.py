from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_noop as _

from geonode.themes.models import (THEME_CACHE_KEY, GeoNodeThemeCustomization,
                                   Partner)


class ADBPOJumbotronSlideShow(models.Model):
    slide_name = models.CharField(max_length=255, unique=True)
    jumbotron_slide_image = models.ImageField(
        upload_to='img/%Y/%m', null=True, blank=True, verbose_name="Jumbotron slide background")
    jumbotron_slide_content = models.TextField(
        null=True, blank=True, verbose_name="Jumbotron slide content", help_text=_("Fill in this section with markdown"))
    hide_jumbotron_slide_content = models.BooleanField(
        default=False,
        verbose_name="Hide text in the jumbotron slide",
        help_text=_("Check this if the jumbotron background image already contains text"))
    is_enabled = models.BooleanField(
        default=True,
        help_text="Disabling this slide will hide it from the slide show")

    def __str__(self):
        get_icon = (lambda arg: '[✓]' if arg else '[✗]')
        return '{} | <Enabled: {} -- Hide Text: {}>'.format(self.slide_name, get_icon(self.is_enabled), get_icon(self.hide_jumbotron_slide_content))


class ADBPOCustomGeonodeTheme(GeoNodeThemeCustomization):
    jumbotron_slide_show = models.ManyToManyField(
        ADBPOJumbotronSlideShow, blank=True)


# Disable other themes if one theme is enabled.
@receiver(post_save, sender=ADBPOCustomGeonodeTheme)
def disable_other(sender, instance, **kwargs):
    if instance.is_enabled:
        ADBPOCustomGeonodeTheme.objects.exclude(
            pk=instance.pk).update(is_enabled=False)


# Invalidate the cached theme if a partner or a theme is updated.
@receiver(post_save, sender=ADBPOCustomGeonodeTheme)
@receiver(post_save, sender=Partner)
@receiver(post_delete, sender=ADBPOCustomGeonodeTheme)
@receiver(post_delete, sender=Partner)
def invalidate_cache(sender, instance, **kwargs):
    cache.delete(THEME_CACHE_KEY)
