# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
# from django.core.exceptions import ValidationError

from .validators import validate_image
from .utilities import get_FilePath
from .utilities import get_ImagePath
# from .validators import valid_extension
# Otros modelos

from activos.models import Equipo


class AnexoArchivo(models.Model):
    equipo = models.ForeignKey(Equipo)
    archivo = models.FileField(upload_to=get_FilePath)
    descripcion = models.CharField(max_length=255, null=True, blank=True)


class AnexoTexto(models.Model):
    equipo = models.ForeignKey(Equipo)
    titulo = models.CharField(max_length=10)
    texto = models.CharField(max_length=255, null=True, blank=True)


class AnexoImagen(models.Model):

    equipo = models.ForeignKey(Equipo)
    ruta = models.ImageField(upload_to=get_ImagePath,
                             validators=[validate_image])
    descripcion = models.CharField(max_length=50, null=True)
