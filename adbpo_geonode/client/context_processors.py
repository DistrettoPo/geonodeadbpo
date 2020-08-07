from collections import OrderedDict

from adbpo_geonode.client.models import MenuItem as mi
from geonode.base.models import Menu


def menus(request):
    menus = {}
    try:
        menus = {
            m: mi.objects.filter(menu=m, is_enabled=True).order_by('order')
            for m in Menu.objects.filter(placeholder__name='TOPBAR_MENU')
        }

    except Exception:
        pass

    return {'adbpo_menus': OrderedDict(menus.items())}
