from django.db import models
from django.utils.translation import gettext_lazy as _
from prototyping.models.license_models import License

def chassis_directory_path(instance, filename):
    return 'chassis/licenza_{0}/{1}/{2}'.format(instance.license_id, instance.creation_date.strftime('%Y/%m/%d'), filename)

class Chassis(models.Model):
    license = models.ForeignKey(License, on_delete=models.CASCADE, verbose_name=_('id_licenza'))
    name = models.CharField(max_length=255, verbose_name=_('nome'))
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('data_creazione'))
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name=_('data_ultima_modifica'))
    file = models.FileField(upload_to=chassis_directory_path, verbose_name=_('file'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('chassis')
        verbose_name_plural = _('chassis')
