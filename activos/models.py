# -*- coding: utf-8 -*-

# Librerias Django:
from __future__ import unicode_literals
from django.db import models

# Otros Modelos:
from seguridad.models import Empresa

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

    def __str__(self):
        return self.clave

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
    padre = models.ForeignKey('self', null=True, blank=True)
    empresa = models.ForeignKey(Empresa, null=True, blank=True)
    sistema = models.CharField(max_length=144, null=True, blank=True)
    ubicacion = models.ForeignKey(Ubicacion, null=True, blank=True)
    imagen = models.ImageField(upload_to='equipos/img', blank=True)
    cliente = models.CharField(max_length=144, null=True, blank=True)
    responsable = models.CharField(max_length=144, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.tag, self.descripcion)

    def get_all_children(self, include_self=True):
        r = []
        if include_self:
            r.append(self)
        for c in Equipo.objects.filter(padre=self):
            _r = c.get_all_children(include_self=True)
            if 0 < len(_r):
                r.extend(_r)
        return r


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
        verbose_name_plural = "Asignaciones"


class Odometro(models.Model):
    equipo = models.ForeignKey(Equipo)
    clave = models.CharField(max_length=144)
    descripcion = models.CharField(max_length=144, null=True)
    udm = models.CharField(max_length=3, choices=ODOMETRO_UDM, null=True)
    esta_activo = models.BooleanField(default=True)

    def __str__(self):
        return "{0} : {1}".format(self.equipo, self.clave)


class Medicion(models.Model):
    odometro = models.ForeignKey(Odometro)
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    lectura = models.DecimalField(max_digits=20, decimal_places=4, default=0.0)

    def __str__(self):
        return "{0} : {1}".format(self.odometro, self.fecha)

    class Meta:
        verbose_name_plural = "Mediciones"


class Archivo(models.Model):
    equipo = models.ForeignKey(Equipo)
    archivo = models.FileField(upload_to='equipos/files', blank=True)


class Texto(models.Model):
    equipo = models.ForeignKey(Equipo)
    texto = models.CharField(max_length=255, null=True, blank=True)


class ImagenAnexo(models.Model):
    equipo = models.ForeignKey(Equipo)
    ruta = models.ImageField(upload_to='equipos/img', blank=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
