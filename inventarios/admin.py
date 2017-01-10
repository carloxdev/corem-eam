# -*- coding: utf-8 -*-

# Librerias Django:
from django.contrib import admin

# Modelos:
from .models import Udm
from .models import Articulo
from .models import Almacen
from .models import Stock


@admin.register(Udm)
class AdminUdm(admin.ModelAdmin):
    list_display = (
        'clave',
        'descripcion'
    )


@admin.register(Articulo)
class AdminArticulo(admin.ModelAdmin):
    list_display = (
        'clave',
        'clave_jde',
        'descripcion',
        'tipo',
        'udm',
    )


@admin.register(Almacen)
class AdminAlmacen(admin.ModelAdmin):
    list_display = (
        'empresa',
        'clave',
        'descripcion',
    )


@admin.register(Stock)
class AdminStock(admin.ModelAdmin):
    list_display = (
        'almacen',
        'articulo',
        'cantidad',
    )
