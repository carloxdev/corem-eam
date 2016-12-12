from __future__ import unicode_literals

from django.db import models

# Otros modelos

from activos.models import Equipo


class AnexoArchivo(models.Model):
    equipo = models.ForeignKey(Equipo)
    archivo = models.FileField(upload_to='equipos/files', blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)


class AnexoTexto(models.Model):
    equipo = models.ForeignKey(Equipo)
    texto = models.CharField(max_length=255, null=True, blank=True)


class AnexoImagen(models.Model):
    equipo = models.ForeignKey(Equipo)
    ruta = models.ImageField(upload_to='equipos/img', blank=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
