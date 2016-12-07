# -*- coding: utf-8 -*-

# Librerias django
from django.contrib import admin

# Modelos:
from .models import OrdenTrabajo
from .models import Actividad
from .models import ManoObra
from .models import Material
from .models import ServicioExterno


@admin.register(OrdenTrabajo)
class AdminOrdenTrabajo(admin.ModelAdmin):
    list_display = (
        'equipo',
        'descripcion',
        'tipo',
        'estado',
        'responsable',
        'fecha_estimada_inicio',
        'fecha_estimada_fin',
        'fecha_real_inicio',
        'fecha_real_fin',
        'observaciones',
        'es_template',
    )


@admin.register(Actividad)
class AdminActividad(admin.ModelAdmin):
    list_display = (
        'orden',
        'numero',
        'descripcion',
        'horas_estimadas',
        'horas_reales',
    )


@admin.register(ManoObra)
class AdminManoObra(admin.ModelAdmin):
    list_display = (
        'orden',
        'empleado',
        'descripcion',
        'fecha_inicio',
        'fecha_fin',
        'horas_estimadas',
        'horas_reales',
    )


@admin.register(Material)
class AdminMaterial(admin.ModelAdmin):
    list_display = (
        'orden',
        'articulo',
        'cantidad_estimada',
        'cantidad_real',
    )


@admin.register(ServicioExterno)
class AdminServicioExterno(admin.ModelAdmin):
    list_display = (
        'orden',
        'clave_jde',
        'descripcion',
    )
