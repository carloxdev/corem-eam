# -*- coding: utf-8 -*-

# Librerias Django:
from __future__ import unicode_literals
from django.db import models

# Otros Modelos:
from seguridad.models import Empresa


class Ubicacion(models.Model):
    clave = models.CharField(max_length=144, null=True)
    descripcion = models.CharField(max_length=144, null=True)

    def __str__(self):
        return self.clave


class Equipo(models.Model):
    tag = models.CharField(max_length=144, null=True)
    descripcion = models.CharField(max_length=144, null=True)
    serie = models.CharField(max_length=144, null=True, blank=True)
    tipo = models.CharField(max_length=144, null=True, blank=True)
    estado = models.CharField(max_length=144, null=True, blank=True)
    padre = models.ForeignKey('self', null=True, blank=True)
    empresa = models.ForeignKey(Empresa, null=True)
    sistema = models.CharField(max_length=144, null=True, blank=True)
    ubicacion = models.ForeignKey(Ubicacion, null=True)
    # cliente =
    # responsable =

    def __str__(self):
        return "{} - {}".format(self.tag, self.descripcion)


class Asignacion(models.Model):
    equipo = models.ForeignKey(Equipo)
    ubicacion = models.ForeignKey(Ubicacion)
    fecha = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
    )

    def __str__(self):
        return "{0} : {1}".format(self.equipo, self.ubicacion)

    class Meta:
        unique_together = (('equipo', 'ubicacion'),)
