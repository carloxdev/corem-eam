# -*- coding: utf-8 -*-

# Django API REST
from rest_framework import filters
from django_filters import CharFilter

# Modelos
from .models import Equipo
from .models import Odometro


class EquipoFilter(filters.FilterSet):

    tag = CharFilter(
        name="tag",
        lookup_expr="contains"
    )

    serie = CharFilter(
        name="serie",
        lookup_expr="contains"
    )

    sistema = CharFilter(
        name="sistema",
        lookup_expr="contains"
    )

    descripcion = CharFilter(
        name="descripcion",
        lookup_expr="contains"
    )

    class Meta:
        model = Equipo
        fields = [
            'tag',
            'serie',
            'estado',
            'padre',
            'sistema',
            'ubicacion',
            'descripcion',
        ]


class OdometroFilter(filters.FilterSet):

    clave = CharFilter(
        name="clave",
        lookup_expr="contains"
    )
    descripcion = CharFilter(
        name="descripcion",
        lookup_expr="contains"
    )
    udm = CharFilter(
        name="udm",
        lookup_expr="contains"
    )

    class Meta:
        model = Odometro
        fields = [
            'equipo',
            'clave',
            'descripcion',
            'udm',
        ]
