# -*- coding: utf-8 -*-

# Django API REST
from rest_framework import filters
from django_filters import CharFilter

# Modelos
from .models import Articulo


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
