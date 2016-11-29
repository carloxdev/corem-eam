# -*- coding: utf-8 -*-

# Librerias Django:
from django.contrib import admin

# Modelos:
from .models import Equipo
from .models import Ubicacion
from .models import Asignacion


@admin.register(Equipo)
class AdminEquipo(admin.ModelAdmin):
    list_display = (
        'tag',
        'descripcion',
        'serie',
        'tipo',
        'estado',
        'padre',
        'empresa',
        'sistema',
        'imagen',
    )


@admin.register(Ubicacion)
class AdminUbicacion(admin.ModelAdmin):
    list_display = (
        'clave',
        'descripcion',
    )


@admin.register(Asignacion)
class AdminAsignacion(admin.ModelAdmin):
    list_display = (
        'equipo',
        'ubicacion',
        'fecha',
    )
