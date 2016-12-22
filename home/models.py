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
from inventarios.models import Articulo


class AnexoArchivo(models.Model):
    equipo = models.ForeignKey(Equipo, null=True, blank=True)
    articulo = models.ForeignKey(Articulo, null=True, blank=True)
    archivo = models.FileField(upload_to=get_FilePath)
    descripcion = models.CharField(max_length=255, null=True, blank=True)


class AnexoTexto(models.Model):
    equipo = models.ForeignKey(Equipo, null=True, blank=True)
    articulo = models.ForeignKey(Articulo, null=True, blank=True)
    titulo = models.CharField(max_length=10)
    texto = models.CharField(max_length=255, null=True, blank=True)


class AnexoImagen(models.Model):

    equipo = models.ForeignKey(Equipo, null=True, blank=True)
    articulo = models.ForeignKey(Articulo, null=True, blank=True)
    ruta = models.ImageField(upload_to=get_ImagePath,
                             validators=[validate_image])
    descripcion = models.CharField(max_length=50, null=True)
