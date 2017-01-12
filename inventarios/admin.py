# -*- coding: utf-8 -*-

# Librerias Django:
from django.contrib import admin

# Modelos:
from .models import UdmArticulo
from .models import Articulo
from .models import Almacen
from .models import Stock


@admin.register(UdmArticulo)
class AdminUdm(admin.ModelAdmin):
    list_display = (
        'clave',
        'descripcion',
        'created_date',
        'updated_date',
    )


@admin.register(Articulo)
class AdminArticulo(admin.ModelAdmin):
    list_display = (
        'clave',
        'clave_jde',
        'descripcion',
        'tipo',
        'udm',
        'created_date',
        'updated_date',
    )


@admin.register(Almacen)
class AdminAlmacen(admin.ModelAdmin):
    list_display = (
        'empresa',
        'clave',
        'descripcion',
        'estado',
        'created_date',
        'updated_date',
    )


@admin.register(Stock)
class AdminStock(admin.ModelAdmin):
    list_display = (
        'almacen',
        'articulo',
        'cantidad',
        'created_date',
        'updated_date',
    )
