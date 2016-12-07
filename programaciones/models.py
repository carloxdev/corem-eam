# -*- coding: utf-8 -*-

# Librerias Django:
from __future__ import unicode_literals
from django.db import models


# Otros Modelos:
from activos.models import Equipo
from activos.models import Odometro

PROGRAMACION_PERIODO_TIPO = (
    ('DIA', 'DIARIO'),
    ('SEM', 'SEMANAL'),
    ('MEN', 'MENSUAL'),
)


class Programa(models.Model):
    equipo = models.ForeignKey(Equipo)
    descripcion = models.CharField(max_length=144, null=True)
    odometro = models.ForeignKey(Odometro, null=True, blank=True)
    odometro_lectura = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        default=0.0
    )
    periodo_tipo = models.CharField(
        max_length=4,
        choices=PROGRAMACION_PERIODO_TIPO,
        default="MEN",
        blank=True
    )
    periodo_cantidad = models.IntegerField()
    fecha_inicio = models.DateField(null=True, blank=True)
    esta_activo = models.BooleanField(default=False)
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{0} : {1}".format(self.equipo, self.descripcion)
