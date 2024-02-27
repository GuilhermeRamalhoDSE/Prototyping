from django.db import models
from django.utils.translation import gettext_lazy as _
from prototyping.models.chassis_models import Chassis

class Element(models.Model):
    chassis = models.ForeignKey(Chassis, on_delete=models.CASCADE, verbose_name=_("ID Chassis"))
    name = models.CharField(max_length=255, verbose_name=_("nome"))
    component_count = models.IntegerField(verbose_name=_("numero di componenti"))

    def __str__(self):
        return f"{self.name} ({self.component_count} componenti)"

    class Meta:
        verbose_name = _("Elemento")
        verbose_name_plural = _("Elementi")
