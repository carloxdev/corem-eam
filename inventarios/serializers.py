# -*- coding: utf-8 -*-

# API REST:
from rest_framework import serializers

# Modelos:
from .models import Almacen
from .models import Articulo


# ----------------- ALMACEN ----------------- #

class AlmacenSerializer(serializers.ModelSerializer):

    estado = serializers.SerializerMethodField()

    class Meta:
        model = Almacen
        fields = (
            'url',
            'pk',
            'clave',
            'descripcion',
            'estado',
            'empresa',
        )

    def get_estado(self, obj):
        try:
            return obj.get_estado_display()
        except:
            return ""


# ----------------- ARTICULO ----------------- #


class ArticuloSerializer(serializers.HyperlinkedModelSerializer):

    tipo = serializers.SerializerMethodField()
    udm = serializers.SerializerMethodField()

    class Meta:
        model = Articulo
        fields = (
            'url',
            'pk',
            'clave',
            'descripcion',
            'tipo',
            'udm',
            'clave_jde',
        )

    def get_tipo(self, obj):
        try:
            return obj.get_tipo_display()
        except:
            return ""

    def get_udm(self, obj):

        try:
            return obj.udm.descripcion
        except:
            return ""
