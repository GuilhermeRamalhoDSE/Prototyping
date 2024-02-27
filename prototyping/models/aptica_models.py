from django.db import models
from django.utils.translation import gettext_lazy as _

class Aptica(models.Model):
    license = models.ForeignKey('License', on_delete=models.CASCADE, verbose_name=_("licenza"))
    hand = models.CharField(max_length=10, choices=[('left', _('sinistra')), ('right', _('destra'))], verbose_name=_("mano"))
    mac_address = models.CharField(max_length=17, verbose_name=_("indirizzo MAC"))

    def __str__(self):
        return f"{self.get_hand_display()} - {self.mac_address}"

    class Meta:
        verbose_name = _("Aptica")
        verbose_name_plural = _("Aptiche")