# -*- coding: utf-8 -*-

# Librerias Django:
from __future__ import unicode_literals
from django.db import models

# Otros Modelos:
from seguridad.models import Empresa
from home.validators import valid_extension


EQUIPO_ESTADO = (
    ('ACT', 'ACTIVO'),
    ('DES', 'DESHABILITADO'),
    ('REP', 'EN REPARACION'),
)

ODOMETRO_UDM = (
    ('HR', 'HORAS'),
    ('KM', 'KILOMETROS'),
    ('K', 'KELVIN'),
    ('C', 'GRADOS CELSIUS'),
    ('F', 'GRADOS FAHRENHEIT'),
)


class Ubicacion(models.Model):
    clave = models.CharField(max_length=144, null=True)
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
        return "{} - {}".format(
            self.clave.encode('utf-8'),
            self.descripcion.encode('utf-8')
        )

    class Meta:
        verbose_name_plural = "Ubicaciones"


class Equipo(models.Model):
    tag = models.CharField(max_length=144, null=True)
    descripcion = models.CharField(max_length=144, null=True)
    serie = models.CharField(max_length=144, null=True, blank=True)
    tipo = models.CharField(max_length=144, null=True, blank=True)
    estado = models.CharField(
        max_length=4,
        choices=EQUIPO_ESTADO,
        default="ACT",
        blank=True
    )
    padre = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    empresa = models.ForeignKey(
        Empresa,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    sistema = models.CharField(max_length=144, null=True, blank=True)
    ubicacion = models.ForeignKey(
        Ubicacion,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    imagen = models.ImageField(
        upload_to='equipos/img',
        blank=True,
        validators=[valid_extension]
    )
    cliente = models.CharField(max_length=144, null=True, blank=True)
    responsable = models.CharField(max_length=144, null=True, blank=True)
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
        return "{0} - {1}".format(self.tag, self.descripcion).encode('utf-8')


class Asignacion(models.Model):
    equipo = models.ForeignKey(Equipo)
    ubicacion = models.ForeignKey(Ubicacion)
    fecha = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
    )

    def __str__(self):
        return "{0} : {1}".format(self.equipo, self.ubicacion).encode('utf-8')

    class Meta:
        unique_together = (('equipo', 'ubicacion'),)
        verbose_name_plural = "Asignaciones"


class UdmOdometro(models.Model):
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
        return "{} - {}".format(
            self.clave.encode('utf-8'),
            self.descripcion.encode('utf-8')
        )


class Odometro(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)
    clave = models.CharField(max_length=144)
    descripcion = models.CharField(max_length=144, null=True)
    udm = models.ForeignKey(UdmOdometro, null=True, on_delete=models.PROTECT)
    esta_activo = models.BooleanField(default=True)
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
        return "{0} : {1}".format(self.equipo, self.clave).encode('utf-8')


class Medicion(models.Model):
    odometro = models.ForeignKey(Odometro, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    lectura = models.DecimalField(max_digits=20, decimal_places=4, default=0.0)
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
        return "{0} : {1}".format(self.odometro, self.fecha).encode('utf-8')

    class Meta:
        verbose_name_plural = "Mediciones"
