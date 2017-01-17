# -*- coding: utf-8 -*-

# Librerias Django:
from __future__ import unicode_literals
from django.db import models

# Otros Modelos:
from activos.models import Equipo
from inventarios.models import Articulo

ORDEN_TIPO = (
    ('PREVE', 'PREVENTIVA'),
    ('PREDI', 'PREDICTIVA'),
    ('CORRE', 'CORRECTIVA'),
)

EQUIPO_ESTADO = (
    ('CAP', 'CAPTURA'),
    ('TER', 'TERMINADA'),
    ('CER', 'CERRADA'),
)


class OrdenTrabajo(models.Model):
    equipo = models.ForeignKey(Equipo)
    descripcion = models.CharField(max_length=144, null=True)
    tipo = models.CharField(
        max_length=6,
        choices=ORDEN_TIPO,
        default="CORRE",
    )

    estado = models.CharField(
        max_length=5,
        choices=EQUIPO_ESTADO,
        default="CAP",
    )

    responsable = models.CharField(max_length=144, null=True, blank=True)
    fecha_estimada_inicio = models.DateTimeField(null=True, blank=True)
    fecha_estimada_fin = models.DateTimeField(null=True, blank=True)
    fecha_real_inicio = models.DateTimeField(null=True, blank=True)
    fecha_real_fin = models.DateTimeField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    es_template = models.BooleanField(default=False)
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )

    def __str__(self):
        return "{0} : {1}".format(self.equipo, self.id).encode('utf-8')

    class Meta:
        verbose_name_plural = "Ordenes de Trabajo"


class Actividad(models.Model):
    orden = models.ForeignKey(OrdenTrabajo)
    numero = models.IntegerField()
    descripcion = models.CharField(max_length=144, null=True)
    horas_estimadas = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0.0
    )
    horas_reales = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0.0
    )
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )

    def __str__(self):
        return "{0} : {1}".format(self.orden, self.numero)

    class Meta:
        verbose_name_plural = "Actividades"
        unique_together = (('orden', 'numero'),)


class ManoObra(models.Model):
    orden = models.ForeignKey(OrdenTrabajo)
    empleado = models.CharField(max_length=144, null=True, blank=True)
    descripcion = models.CharField(max_length=144, null=True, blank=True)
    fecha_inicio = models.DateTimeField(null=True)
    fecha_fin = models.DateTimeField(null=True)
    horas_estimadas = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0.0
    )
    horas_reales = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0.0
    )
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )

    def __str__(self):
        return "{0} : {1}".format(self.orden, self.empleado)

    class Meta:
        verbose_name_plural = "Mano de Obra"


class Material(models.Model):
    orden = models.ForeignKey(OrdenTrabajo)
    articulo = models.ForeignKey(Articulo)
    cantidad_estimada = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0
    )
    cantidad_real = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0
    )
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )

    def __str__(self):
        return "{0} : {1}".format(self.orden, self.articulo)

    class Meta:
        verbose_name_plural = "Materiales"


class ServicioExterno(models.Model):
    orden = models.ForeignKey(OrdenTrabajo)
    clave_jde = models.CharField(max_length=144, null=True)
    descripcion = models.CharField(max_length=144, null=True)
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )

    def __str__(self):
        return "{0} : {1}".format(self.orden, self.clave_jde)

    class Meta:
        verbose_name_plural = "Servicios Externos"
