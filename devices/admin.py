from django.contrib import admin

# Register your models here.

from devices.models import Device


class DeviceAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('id', 'name', 'api_key', 'enable', 'remote_address')


admin.site.register(Device, DeviceAdmin)
