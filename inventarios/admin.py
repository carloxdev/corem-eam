# -*- coding: utf-8 -*-

# Librerias Django:
from django.contrib import admin

# Modelos:
from .models import UdmArticulo
from .models import Articulo
from .models import Almacen
from .models import Stock
from .models import MovimientoCabecera
from .models import MovimientoDetalle


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


@admin.register(UdmArticulo)
class AdminUdmArticulo(admin.ModelAdmin):
    list_display = (
        'clave',
        'descripcion',
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


@admin.register(MovimientoCabecera)
class AdminMovientoCabecera(admin.ModelAdmin):
    list_display = (
        'pk',
        'fecha',
        'descripcion',
        'almacen_origen',
        'almacen_destino',
        'persona_recibe',
        'persona_entrega',
        'estado',
        'tipo',
        'clasificacion',
        'orden_trabajo',
        'usuario',
    )


@admin.register(MovimientoDetalle)
class AdminMovimientoDetalle(admin.ModelAdmin):
    list_display = (
        'pk',
        'articulo',
        'cantidad',
        'cabecera',
    )
