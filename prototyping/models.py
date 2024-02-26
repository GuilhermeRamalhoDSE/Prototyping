from django.db import models
from django.utils.translation import gettext_lazy as _

class LicenseManagementDse(models.Model):
    customer_id = models.AutoField(primary_key=True, verbose_name=_("Customer ID"))
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    email = models.EmailField(verbose_name=_("Email"))
    address = models.CharField(max_length=255, verbose_name=_("Address"), null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name=_("Telephone"), null=True, blank=True)
    license_code = models.CharField(max_length=100, unique=True, verbose_name=_("License Code"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))
    start_date = models.DateField(verbose_name=_("Start Date"))
    expiration_date = models.DateField(verbose_name=_("Expiration Date"))

    class Meta:
        verbose_name = _("License Management DSE")
        verbose_name_plural = _("Licenses Management DSE")

    def __str__(self):
        return self.name
