import binascii
import os

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Device(models.Model):
    """
    Requests for iot device Gateway
    """
    name = models.CharField(_('Device name'), max_length=60, help_text=_('Enter the device name'))
    field_1 = models.CharField(_('Area 1'), max_length=20, null=True, blank=True)
    field_id_1 = models.CharField(_('Area ID 1'), max_length=30, null=True, blank=True)
    field_2 = models.CharField(_('Area 2'), max_length=20, null=True, blank=True)
    field_id_2 = models.CharField(_('Area ID 2'), max_length=30, null=True, blank=True)
    field_3 = models.CharField(_('Area 3'), max_length=20, null=True, blank=True)
    field_id_3 = models.CharField(_('Area ID 3'), max_length=30, null=True, blank=True)
    field_4 = models.CharField(_('Area 4'), max_length=20, null=True, blank=True)
    field_id_4 = models.CharField(_('Area ID 4'), max_length=30, null=True, blank=True)
    field_5 = models.CharField(_('Area 5'), max_length=20, null=True, blank=True)
    field_id_5 = models.CharField(_('Area ID 5'), max_length=30, null=True, blank=True)
    field_6 = models.CharField(_('Area 6'), max_length=20, null=True, blank=True)
    field_id_6 = models.CharField(_('Area ID 6'), max_length=30, null=True, blank=True)
    field_7 = models.CharField(_('Area 7'), max_length=20, null=True, blank=True)
    field_id_7 = models.CharField(_('Area ID 7'), max_length=30, null=True, blank=True)
    field_8 = models.CharField(_('Area 8'), max_length=20, null=True, blank=True)
    field_id_8 = models.CharField(_('Area ID 8'), max_length=30, null=True, blank=True)
    field_9 = models.CharField(_('Area 9'), max_length=20, null=True, blank=True)
    field_id_9 = models.CharField(_('Area ID 9'), max_length=30, null=True, blank=True)
    field_10 = models.CharField(_('Area 10'), max_length=20, null=True, blank=True)
    field_id_10 = models.CharField(_('Area ID 10'), max_length=30, null=True, blank=True)
    api_key = models.CharField(_('Api key'), max_length=200)  # api key
    description = models.TextField(_('Explanation'), blank=True, max_length=255)
    enable = models.BooleanField(_('Activate'), default=True)
    remote_address = models.CharField(_('IP address'), max_length=255)
    pub_date = models.DateTimeField(_('Release date'), auto_now=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.api_key:
            self.api_key = self.generate_key()

        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(12)).decode()
