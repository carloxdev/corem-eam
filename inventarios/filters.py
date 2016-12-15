# -*- coding: utf-8 -*-

# Django API REST
from rest_framework import filters
from django_filters import CharFilter

# Modelos
from .models import Articulo


class ArticuloFilter(filters.FilterSet):

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
            'clave_jde',
            'descripcion',
            'tipo',
        ]
