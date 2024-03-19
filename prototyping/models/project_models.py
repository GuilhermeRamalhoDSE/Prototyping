from django.db import models
from django.utils.translation import gettext_lazy as _
from prototyping.models.client_models import Client
from prototyping.models.user_models import User
from django.utils.timezone import now

class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=_("cliente"))
    name = models.CharField(max_length=255, verbose_name=_("nome"))
    start_date = models.DateField(verbose_name=_("data inizio"), default=now)
    end_date = models.DateField(verbose_name=_("data fine"), null=True, blank=True) 
    users = models.ManyToManyField(User, verbose_name=_("utenti"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Progetto")
        verbose_name_plural = _("Progetti")
