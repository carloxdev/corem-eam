# -*- coding: utf-8 -*-

# API REST:
from rest_framework import serializers

# Modelos:
from .models import Almacen
from .models import Articulo
from .models import EntradaCabecera
from .models import EntradaDetalle
from .models import SalidaCabecera


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


# ----------------- ENTRADA ----------------- #


class EntradaCabeceraSerializer(serializers.HyperlinkedModelSerializer):

    almacen = serializers.SerializerMethodField()

    class Meta:
        model = EntradaCabecera
        fields = (
            'pk',
            'url',
            'clave',
            'fecha',
            'descripcion',
            'almacen'
        )

    def get_almacen(self, obj):

        try:
            return "({}) {}".format(
                obj.almacen.clave.encode("utf-8"),
                obj.almacen.descripcion.encode("utf-8")
            )
        except:
            return ""


class EntradaDetalleSerializer(serializers.ModelSerializer):

    articulo_clave = serializers.SerializerMethodField()

    class Meta:
        model = EntradaDetalle
        fields = (
            'pk',
            'url',
            'cantidad',
            'articulo',
            'cabecera',
            'articulo_clave',
        )

    def get_articulo_clave(self, obj):

        try:
            return "({}) {}".format(
                obj.articulo.clave.encode("utf-8"),
                obj.articulo.descripcion.encode("utf-8")
            )
        except:
            return ""

# ----------------- SALIDA ----------------- #


class SalidaCabeceraSerializer(serializers.HyperlinkedModelSerializer):

    almacen = serializers.SerializerMethodField()

    class Meta:
        model = SalidaCabecera
        fields = (
            'url',
            'pk',
            'clave',
            'fecha',
            'descripcion',
            'almacen'
        )

    def get_almacen(self, obj):

        try:
            return "({}) {}".format(
                obj.almacen.clave.encode("utf-8"),
                obj.almacen.descripcion.encode("utf-8")
            )
        except:
            return ""
