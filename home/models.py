from __future__ import unicode_literals

from django.db import models

# Otros modelos

from activos.models import Equipo


class Archivo(models.Model):
    equipo = models.ForeignKey(Equipo)
    archivo = models.FileField(upload_to='equipos/files', blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)


class Texto(models.Model):
    equipo = models.ForeignKey(Equipo)
    texto = models.CharField(max_length=255, null=True, blank=True)


class ImagenAnexo(models.Model):
    equipo = models.ForeignKey(Equipo)
    ruta = models.ImageField(upload_to='equipos/img', blank=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
