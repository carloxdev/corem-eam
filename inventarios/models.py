# -*- coding: utf-8 -*-

# Librerias Django:
from __future__ import unicode_literals
from django.db import models

# Otros Modelos:
from seguridad.models import Empresa


ARTICULO_TIPO = (
    ('INS', 'INSUMO'),
    ('HER', 'HERRAMIENTA'),
    ('ACT', 'ACTIVO'),
    ('REF', 'REFACCION'),
)


class Udm(models.Model):
    clave = models.CharField(max_length=144, null=True)
    descripcion = models.CharField(max_length=144, null=True)

    def __str__(self):
        return self.clave


class Articulo(models.Model):
    clave = models.CharField(max_length=144, null=True)
    descripcion = models.CharField(max_length=144, null=True)
    tipo = models.CharField(
        max_length=6,
        choices=ARTICULO_TIPO,
        default="CORRE",
        blank=True
    )
    udm = models.ForeignKey(Udm, null=True)
    clave_jde = models.CharField(max_length=144, null=True)

    def __str__(self):
        return "{0} : {1}".format(
            self.clave_jde,
            self.descripcion
        ).encode('utf-8')

    class Meta:
        verbose_name_plural = "Articulo"


class Almacen(models.Model):
    empresa = models.ForeignKey(Empresa, null=True, blank=True)
    clave = models.CharField(max_length=144, null=True)
    descripcion = models.CharField(max_length=144, null=True)
    articulos = models.ManyToManyField(
        Articulo,
        through="Stock",
        blank=True
    )

    def __str__(self):
        return "{0} : {1}".format(self.clave, self.descripcion)

    class Meta:
        verbose_name_plural = "Almacenes"


class Stock(models.Model):
    almacen = models.ForeignKey(Almacen)
    articulo = models.ForeignKey(Articulo)
    cantidad = models.CharField(max_length=140)

    def __str__(self):
        return "{0} - {1}".format(self.almacen, self.articulo)

    class Meta:
        unique_together = (('almacen', 'articulo'),)
