# -*- coding: utf-8 -*-

# Librerias Django:
from __future__ import unicode_literals
from django.db import models

# Otros Modelos:
from seguridad.models import Empresa
from activos.models import Equipo


class OrdenTrabajo(models.Model):
    empresa = models.ForeignKey(Empresa)
    equipo = models.ForeignKey(Equipo)
    descripcion = models.CharField(max_length=144, null=True)
    tipo = models.CharField(max_length=144, null=True)
    estado = models.CharField(max_length=144, null=True)
    # responsable
    fecha_estimada_inicio = models.DateTimeField(null=True)
    fecha_estimada_fin = models.DateTimeField(null=True)
    fecha_real_inicio = models.DateTimeField(null=True)
    fecha_real_fin = models.DateTimeField(null=True)
    es_template = models.BooleanField(default=False)
    # Fallas
