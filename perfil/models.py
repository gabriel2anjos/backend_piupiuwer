from django.db import models
from django.contrib.auth.models import User, Group, Permission

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='perfil_relacionado')
    foto_perfil = models.URLField(max_length=300,blank=True)