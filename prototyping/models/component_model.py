from django.db import models
from django.utils.translation import gettext_lazy as _
from prototyping.models.element_models import Element
from django.utils.timezone import now

def component_directory_path(instance, filename):
    return 'component/element_{0}/{1}/{2}'.format(instance.element_id, instance.created_at.strftime('%Y/%m/%d'), filename)


class Component(models.Model):
    version_id = models.IntegerField(verbose_name=_("id_versione"))
    element = models.ForeignKey(Element, on_delete=models.CASCADE, verbose_name=_("elemento"), null=True)
    name = models.CharField(max_length=255, verbose_name=_("nome"))
    file = models.FileField(upload_to=component_directory_path, verbose_name=_("file"), null=True, blank=True)
    limit_position_x = models.FloatField(verbose_name=_("limite posizione x"), null=True, blank=True)
    limit_position_y = models.FloatField(verbose_name=_("limite posizione y"), null=True, blank=True)
    limit_position_z = models.FloatField(verbose_name=_("limite posizione z"), null=True, blank=True)
    limit_rotation_x = models.FloatField(verbose_name=_("limite rotazione x"), null=True, blank=True)
    limit_rotation_y = models.FloatField(verbose_name=_("limite rotazione y"), null=True, blank=True)
    limit_rotation_z = models.FloatField(verbose_name=_("limite rotazione z"), null=True, blank=True)
    limit_rotation_w = models.FloatField(verbose_name=_("limite rotazione w"), null=True, blank=True)
    area_radius = models.FloatField(verbose_name=_("area/raggio"))
    haptic_stiffness = models.FloatField(verbose_name=_("aptic stifness"))
    haptic_temperature = models.FloatField(verbose_name=_("aptic temperature"))
    haptic_texture = models.IntegerField(verbose_name=_("aptic texture"))
    created_at = models.DateTimeField(verbose_name=_("data di creazione"), default=now)
 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Componente")
        verbose_name_plural = _("Componenti")
