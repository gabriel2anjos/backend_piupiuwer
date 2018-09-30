from django.db import models
from django.contrib.auth.models import User, Group, Permission
import datetime
# Create your models here.
class Piu(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    favoritado = models.BooleanField(default = False)
    conteudo = models.CharField(max_length = 200, null=False)
    data = models.DateTimeField('Data', null=False, blank=False,default=datetime.datetime.now)