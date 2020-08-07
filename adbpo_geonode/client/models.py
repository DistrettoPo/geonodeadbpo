from django.db import models
from django.utils.translation import ugettext_noop as _
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from geonode.base.models import MenuItem


class MenuItem(MenuItem):
    icon = models.ImageField(
        upload_to='img/%Y/%m', verbose_name="Icon Image")
    icon_thumbnail = ImageSpecField(source='icon', processors=[ResizeToFill(142, 142)], options={'quality': 80})
    is_enabled = models.BooleanField(
        default=True,
        help_text=_("Disabling this will hide the link from the home page quick filter links"))
