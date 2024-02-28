from django.db import models
from django.utils.translation import gettext_lazy as _

class Component(models.Model):
    version_id = models.IntegerField(verbose_name=_("id_versione"))
    name = models.CharField(max_length=255, verbose_name=_("nome"))
    position_x = models.FloatField(verbose_name=_("posizione x"))
    limit_position_x = models.FloatField(verbose_name=_("limite posizione x"))
    position_y = models.FloatField(verbose_name=_("posizione y"))
    limit_position_y = models.FloatField(verbose_name=_("limite posizione y"))
    position_z = models.FloatField(verbose_name=_("posizione z"))
    limit_position_z = models.FloatField(verbose_name=_("limite posizione z"))
    rotation_x = models.FloatField(verbose_name=_("rotazione x"))
    limit_rotation_x = models.FloatField(verbose_name=_("limite rotazione x"))
    rotation_y = models.FloatField(verbose_name=_("rotazione y"))
    limit_rotation_y = models.FloatField(verbose_name=_("limite rotazione y"))
    rotation_z = models.FloatField(verbose_name=_("rotazione z"))
    limit_rotation_z = models.FloatField(verbose_name=_("limite rotazione z"))
    rotation_w = models.FloatField(verbose_name=_("rotazione w"))
    limit_rotation_w = models.FloatField(verbose_name=_("limite rotazione w"))
    area_radius = models.FloatField(verbose_name=_("area/raggio"))
    haptic_stiffness = models.FloatField(verbose_name=_("aptic stifness"))
    haptic_temperature = models.FloatField(verbose_name=_("aptic temperature"))
    haptic_texture = models.IntegerField(verbose_name=_("aptic texture"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Componente")
        verbose_name_plural = _("Componenti")
