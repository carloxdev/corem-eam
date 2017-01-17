# -*- coding: utf-8 -*-

# Django API REST
from rest_framework import filters
from django_filters import CharFilter
from django_filters import DateFilter
# from django_filters import NumberFilter

# Modelos
from .models import Articulo
from .models import MovimientoCabecera
from .models import Stock


class ArticuloFilter(filters.FilterSet):

    clave = CharFilter(
        name="clave",
        lookup_expr="contains"
    )

    clave_jde = CharFilter(
        name="clave_jde",
        lookup_expr="contains"
    )

    descripcion = CharFilter(
        name="descripcion",
        lookup_expr="contains"
    )

    class Meta:
        model = Articulo
        fields = [
            'clave',
            'descripcion',
            'tipo',
            'clave_jde',
        ]


class StockFilter(filters.FilterSet):

    cantidad_mayorque = CharFilter(
        name="cantidad",
        lookup_expr="gte"
    )

    cantidad_menorque = CharFilter(
        name="cantidad",
        lookup_expr="lte"
    )

    class Meta:
        model = Stock
        fields = [
            'articulo',
            'almacen',
            'cantidad_mayorque',
            'cantidad_menorque',
        ]


class MovimientoCabeceraFilter(filters.FilterSet):

    fecha_inicio = DateFilter(
        name="fecha",
        lookup_expr="gte"
    )
    fecha_fin = DateFilter(
        name="fecha",
        lookup_expr="lte"
    )
    descripcion = CharFilter(
        name="descripcion",
        lookup_expr="contains"

    )
    persona_resibe = CharFilter(
        name="persona_recibe",
        lookup_expr="contains"

    )
    persona_entrega = CharFilter(
        name="persona_entrega",
        lookup_expr="contains"

    )
    clave = CharFilter(
        name="clave",
        lookup_expr="contains"

    )

    class Meta:
        model = MovimientoCabecera
        fields = [
            'almacen_origen',
            'almacen_destino',
            'estado',
            'tipo',
        ]
