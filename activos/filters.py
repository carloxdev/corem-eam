# -*- coding: utf-8 -*-

# Django API REST
from rest_framework import filters
# import django_filters

# Modelos
from .models import Equipo


class EquipoFilter(filters.FilterSet):

    class Meta:
        model = Equipo
        fields = [
            'tag',
            'descripcion',
        ]
