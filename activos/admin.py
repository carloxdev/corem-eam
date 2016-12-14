# -*- coding: utf-8 -*-

# Librerias Django:
from django.contrib import admin

# Modelos:
from .models import Equipo
from .models import Ubicacion
from .models import Asignacion
from .models import Odometro
from .models import Medicion

# Import-Export
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class EquipoResource(resources.ModelResource):
    class Meta:
        model = Equipo
        fields = (
            'id',
            'tag',
            'descripcion',
            'serie',
            'tipo',
            'estado',
            'padre',
            'empresa',
            'sistema',
            'cliente',
            'responsable',
        )


@admin.register(Equipo)
class AdminEquipo(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EquipoResource
    list_display = (
        'id',
        'tag',
        'descripcion',
        'serie',
        'tipo',
        'estado',
        'padre',
        'empresa',
        'sistema',
        'cliente',
        'responsable',
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


@admin.register(Odometro)
class Odometro(admin.ModelAdmin):
    list_display = (
        'equipo',
        'clave',
        'descripcion',
        'udm',
        'esta_activo',
    )


@admin.register(Medicion)
class Medicion(admin.ModelAdmin):
    list_display = (
        'odometro',
        'fecha',
        'lectura',
    )
