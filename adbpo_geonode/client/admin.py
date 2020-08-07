from django.contrib import admin
from adbpo_geonode.client.models import MenuItem as mi
from geonode.base.models import MenuItem, Menu
from geonode.base.admin import MenuAdmin


@admin.register(mi)
class MenuItemAdmin(admin.ModelAdmin):
    pass


class ADBPOMenuAdmin(MenuAdmin):
    pass


admin.site.unregister(MenuItem)
admin.site.unregister(Menu)
admin.site.register(Menu, ADBPOMenuAdmin)
