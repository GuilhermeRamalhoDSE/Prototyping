from django.db import models
from prototyping.models.license_models import License

class User(models.Model):
    license = models.ForeignKey(
        License,
        on_delete=models.CASCADE,
        verbose_name='License ID',  # Atualizado para inglês
        related_name='users'
    )
    first_name = models.CharField(max_length=255, verbose_name='First Name')  
    last_name = models.CharField(max_length=255, verbose_name='Last Name')  
    email = models.EmailField(unique=True, verbose_name='Email')
    role = models.CharField(max_length=255, verbose_name='Role') 
    password = models.CharField(max_length=255, verbose_name='Password')  

    class Meta:
        verbose_name = 'User'  
        verbose_name_plural = 'Users'  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
