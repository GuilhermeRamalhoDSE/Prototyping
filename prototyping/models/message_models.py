from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from prototyping.models.project_models import Project
from prototyping.models.client_models import Client

class Message(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=_("cliente"))
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=_("progetto"))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("utente"))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_("data"))
    message = models.TextField(verbose_name=_("messaggio"))
    is_read = models.BooleanField(default=False, verbose_name=_("letto"))

    def __str__(self):
        return f"Message from {self.user} on {self.date}"

    class Meta:
        verbose_name = _("Messaggio")
        verbose_name_plural = _("Messaggi")
