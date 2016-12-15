# -*- coding: utf-8 -*-

# API REST:
from rest_framework import serializers

# Modelos:
from .models import Almacen
from .models import Articulo


# ----------------- ALMACEN ----------------- #

class AlmacenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Almacen
        fields = (
            'url',
            'pk',
            'empresa',
            'clave',
            'descripcion',
        )


# ----------------- ARTICULO ----------------- #


class ArticuloSerializer(serializers.HyperlinkedModelSerializer):

    tipo = serializers.SerializerMethodField()

    class Meta:
        model = Articulo
        fields = (
            'url',
            'pk',
            'clave_jde',
            'descripcion',
            'tipo',
            'udm',
        )

    def get_tipo(self, obj):
        try:
            return obj.get_tipo_display()
        except:
            return ""
