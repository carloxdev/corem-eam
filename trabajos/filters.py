# -*- coding: utf-8 -*-

# Django API REST
from rest_framework import filters
from django_filters import CharFilter

# Modelos
from .models import OrdenTrabajo


class OrdenTrabajoFilter(filters.FilterSet):

    class Meta:
        model = OrdenTrabajo
        fields = [
            'id',
            'equipo',
            'descripcion',
            'tipo',
            'estado',
            'responsable',
        ]
