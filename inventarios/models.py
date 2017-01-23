# -*- coding: utf-8 -*-

# Librerias Django:
from __future__ import unicode_literals
from django.db import models

# Otros Modelos:
from seguridad.models import Empresa

# Validadores:
from home.validators import valid_extension
from home.validators import validate_image

ARTICULO_TIPO = (
    ('INS', 'INSUMO'),
    ('HER', 'HERRAMIENTA'),
    ('ACT', 'ACTIVO'),
    ('REF', 'REFACCION'),
)

ARTICULO_ESTADO = (
    ('ACT', 'ACTIVO'),
    ('DES', 'DESHABILITADO'),
)

ALMACEN_ESTADO = (
    ('ACT', 'ACTIVO'),
    ('DES', 'DESHABILITADO'),
)

MOVIMIENTO_ESTADO = (
    ('CAP', 'CAPTURA'),
    ('CER', 'CERRADO'),
)

MOVIMIENTO_TIPO = (
    ('ENT', 'ENTRADA'),
    ('SAL', 'SALIDA'),
)


class UdmArticulo(models.Model):
    clave = models.CharField(max_length=144, unique=True)
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
        return "({}) {}".format(
            self.clave.encode('utf-8'),
            self.descripcion.encode('utf-8')
        )


class Articulo(models.Model):
    clave = models.CharField(max_length=144, null=True)
    descripcion = models.CharField(max_length=144, null=True)
    estado = models.CharField(
        max_length=4,
        choices=ARTICULO_ESTADO,
        default="ACT",
    )
    tipo = models.CharField(
        max_length=6,
        choices=ARTICULO_TIPO,
        default="CORRE",
        blank=True
    )
    imagen = models.ImageField(
        upload_to='articulos/img',
        blank=True,
        null=True,
        validators=[
            valid_extension,
            validate_image
        ]
    )
    udm = models.ForeignKey(
        UdmArticulo,
        on_delete=models.PROTECT
    )
    clave_jde = models.CharField(max_length=144, blank=True, null=True)
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
        return "({0}) {1}".format(
            self.clave,
            self.descripcion
        ).encode('utf-8')

    class Meta:
        verbose_name_plural = "Articulo"


class Almacen(models.Model):
    empresa = models.ForeignKey(
        Empresa, null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    clave = models.CharField(max_length=144, null=True)
    descripcion = models.CharField(max_length=144, null=True)
    estado = models.CharField(
        max_length=4,
        choices=ALMACEN_ESTADO,
        default="ACT",
        blank=True
    )
    articulos = models.ManyToManyField(
        Articulo,
        through="Stock",
        blank=True
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
        return "{0} : {1}".format(
            self.clave.encode('utf-8'),
            self.descripcion.encode('utf-8')
        )

    class Meta:
        verbose_name_plural = "Almacenes"


class Stock(models.Model):
    almacen = models.ForeignKey(Almacen, on_delete=models.PROTECT)
    articulo = models.ForeignKey(Articulo, on_delete=models.PROTECT)
    costo = models.DecimalField(
        max_digits=20, decimal_places=4, default=0.0
    )
    cantidad = models.DecimalField(
        max_digits=20, decimal_places=4, default=0.0)
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
        return "{0}) {1}".format(self.almacen, self.articulo)

    class Meta:
        unique_together = (('almacen', 'articulo'),)


class MovimientoCabecera(models.Model):
    fecha = models.DateTimeField()
    descripcion = models.CharField(max_length=144)
    almacen_origen = models.ForeignKey(
        Almacen, related_name="origen", null=True, blank=True)
    almacen_destino = models.ForeignKey(Almacen, related_name="destino")
    persona_recibe = models.CharField(max_length=144, blank=True)
    persona_entrega = models.CharField(max_length=144, blank=True)
    estado = models.CharField(
        max_length=4,
        choices=MOVIMIENTO_ESTADO,
        default="CAP",
        blank=True
    )
    tipo = models.CharField(
        max_length=4,
        choices=MOVIMIENTO_TIPO,
    )

    def __str__(self):
        return self.descripcion.encode('utf-8')


class MovimientoDetalle(models.Model):
    cantidad = models.DecimalField(
        max_digits=20, decimal_places=4, default=0.0)
    articulo = models.ForeignKey(Articulo)
    cabecera = models.ForeignKey(MovimientoCabecera)
