# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from django.core.exceptions import ValidationError

# Otros modelos

from activos.models import Equipo


class AnexoArchivo(models.Model):
    equipo = models.ForeignKey(Equipo)
    archivo = models.FileField(upload_to='equipos/files',
                               blank=True, default='equipos/img/no-image.png')
    descripcion = models.CharField(max_length=255, null=True, blank=True)


class AnexoTexto(models.Model):
    equipo = models.ForeignKey(Equipo)
    titulo = models.CharField(max_length=10)
    texto = models.CharField(max_length=255, null=True, blank=True)


class AnexoImagen(models.Model):

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Tamaño Máximo de Archivo %sMB" %
                                  str(megabyte_limit))

    equipo = models.ForeignKey(Equipo)
    ruta = models.ImageField(upload_to='equipos/img',
                             validators=[validate_image])
    descripcion = models.CharField(max_length=50)
