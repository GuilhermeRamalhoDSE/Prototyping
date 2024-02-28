from django.db import models
from django.utils.translation import gettext_lazy as _
from prototyping.models.client_models import Client
from prototyping.models.user_models import User


class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=_("cliente"))
    name = models.CharField(max_length=255, verbose_name=_("nome"))
    creation_date = models.DateField(verbose_name=_("data creazione"))
    last_release_date = models.DateField(verbose_name=_("data ultima modifica"))
    users = models.ManyToManyField(User, verbose_name=_("utenti"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Progetto")
        verbose_name_plural = _("Progetti")