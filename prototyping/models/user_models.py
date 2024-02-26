from django.db import models
from prototyping.models.license_models import LicenseManagementDse

class User(models.Model):
    license_id = models.ForeignKey(
        LicenseManagementDse,
        on_delete=models.CASCADE,
        verbose_name='ID Cliente',
        related_name='users'
    )
    first_name = models.CharField(max_length=255, verbose_name='Nome')
    last_name = models.CharField(max_length=255, verbose_name='Cognome')
    email = models.EmailField(unique=True, verbose_name='Email')
    role = models.CharField(max_length=255, verbose_name='Ruolo')
    password = models.CharField(max_length=255, verbose_name='Password')
    
    class Meta:
        verbose_name = 'Utente'
        verbose_name_plural = 'Utenti'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
