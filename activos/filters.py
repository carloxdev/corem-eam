# -*- coding: utf-8 -*-

# Django API REST
from rest_framework import filters
# import django_filters


# Modelos
from .models import Ubicacion


class UbicacionFilter(filters.FilterSet):

    # fecha_operacion_min = django_filters.CharFilter(
    #     action=filtra_FechaOperacion_Min)
    # fecha_operacion_max = django_filters.CharFilter(
    #     action=filtra_FechaOperacion_Max)

    class Meta:
        model = Ubicacion
        fields = [
            'id',
        ]
