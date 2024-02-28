from django.db import models
from django.utils.translation import gettext_lazy as _
from prototyping.models.client_models import Client
from prototyping.models.project_models import Project

def release_directory_path(instance, filename):
    return 'releases/client_{0}/project_{1}/{2}'.format(instance.client.id, instance.project.id, instance.creation_date.strftime('%Y/%m/%d'), filename)

class Release(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=_("id_cliente"))
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=_("id_progetto"))
    name = models.CharField(max_length=255, verbose_name=_("nome"))
    file = models.FileField(upload_to=release_directory_path, verbose_name=_("file"))
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_("data creazione"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Release")
        verbose_name_plural = _("Releases")
