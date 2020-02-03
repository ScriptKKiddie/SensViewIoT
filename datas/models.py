from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _

from devices.models import Device


class Data(models.Model):
    """
    """
    device = models.ForeignKey(Device, related_name='device_data', on_delete=models.CASCADE)
    field_1 = models.CharField(_('Value 1'), max_length=10, null=True, blank=False)
    field_2 = models.CharField(_('Value 2'), max_length=10, null=True, blank=False)
    field_3 = models.CharField(_('Value 3'), max_length=10, null=True, blank=False)
    field_4 = models.CharField(_('Value 4'), max_length=10, null=True, blank=False)
    field_5 = models.CharField(_('Value 5'), max_length=10, null=True, blank=False)
    field_6 = models.CharField(_('Value 6'), max_length=10, null=True, blank=False)
    field_7 = models.CharField(_('Value 7'), max_length=10, null=True, blank=False)
    field_8 = models.CharField(_('Value 8'), max_length=10, null=True, blank=False)
    field_9 = models.CharField(_('Value 9'), max_length=10, null=True, blank=False)
    field_10 = models.CharField(_('Value 10'), max_length=10, null=True, blank=False)
    api_key = models.CharField(_('API key'), max_length=200, null=True, blank=True)  # api key
    remote_address = models.CharField(_('IP address'), max_length=255)
    pub_date = models.DateTimeField(_('Release date'), auto_now=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.device.name

