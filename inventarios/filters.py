# -*- coding: utf-8 -*-

# Django API REST
from rest_framework import filters
from django_filters import CharFilter
from django_filters import DateFilter
# from django_filters import NumberFilter

# Modelos
from .models import Articulo
from .models import EntradaCabecera


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


class EntradaCabeceraFilter(filters.FilterSet):
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
    descripcion = CharFilter(
        name="descripcion",
        lookup_expr="contains"

    )
    clave = CharFilter(
        name="clave",
        lookup_expr="contains"

    )

    class Meta:
        model = EntradaCabecera
        fields = [
            'almacen',
        ]