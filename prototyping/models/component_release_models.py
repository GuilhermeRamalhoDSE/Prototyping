from django.db import models
from prototyping.models.release_models import Release
from prototyping.models.chassis_models import Chassis
from prototyping.models.element_models import Element
from prototyping.models.component_model import Component

def component_release_file_path(instance, filename):
    return f'release_{instance.release.id}/component_{instance.component.id}/{filename}'

class ComponentRelease(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE, verbose_name="Release")
    chassis = models.ForeignKey(Chassis, on_delete=models.CASCADE, verbose_name="Chassis")
    element = models.ForeignKey(Element, on_delete=models.CASCADE, verbose_name="Element")
    component = models.ForeignKey(Component, on_delete=models.CASCADE, verbose_name="Component")
    file = models.FileField(upload_to=component_release_file_path, verbose_name="File")

    class Meta:
        verbose_name = "Component Release"
        verbose_name_plural = "Component Releases"

    def __str__(self):
        return f"{self.release} - {self.component}"
