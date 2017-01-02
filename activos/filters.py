# -*- coding: utf-8 -*-

# Django API REST
from rest_framework import filters
from django_filters import CharFilter
from django_filters import DateFilter
from django_filters import NumberFilter

# Modelos
from .models import Equipo
from .models import Odometro
from .models import Medicion


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


class MedicionFilter(filters.FilterSet):
    fecha_min = DateFilter(
        name="fecha",
        lookup_expr="gte"
    )
    fecha_max = DateFilter(
        name="fecha",
        lookup_expr="lte"
    )
    lectura_min = NumberFilter(
        name="lectura",
        lookup_expr="gte"
    )
    lectura_max = NumberFilter(
        name="lectura",
        lookup_expr="lte"
    )

    class Meta:
        model = Medicion
        fields = [
            'odometro',
        ]
