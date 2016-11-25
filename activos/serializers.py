# -*- coding: utf-8 -*-

# API REST:
from rest_framework import serializers

# Modelos:
from .models import Equipo


class EquipoSerializer(serializers.HyperlinkedModelSerializer):

    padre = serializers.SerializerMethodField()
    empresa = serializers.SerializerMethodField()
    ubicacion = serializers.SerializerMethodField()

    class Meta:
        model = Equipo
        fields = (
            'tag',
            'descripcion',
            'serie',
            'tipo',
            'estado',
            'padre',
            'empresa',
            'sistema',
            'ubicacion',
        )

    def get_padre(self, obj):

        try:
            return obj.padre.tag
        except:
            return ""

    def get_empresa(self, obj):

        try:
            return obj.empresa.clave
        except:
            return ""

    def get_ubicacion(self, obj):

        try:
            return obj.ubicacion.clave
        except:
            return ""
