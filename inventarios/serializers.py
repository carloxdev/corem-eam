# -*- coding: utf-8 -*-

# API REST:
from rest_framework import serializers

# Modelos:
from .models import Almacen
from .models import Stock
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


# ----------------- STOCK ----------------- #

class StockSerializer(serializers.ModelSerializer):

    estado = serializers.SerializerMethodField()
    almacen = serializers.SerializerMethodField()
    articulo = serializers.SerializerMethodField()

    class Meta:
        model = Stock
        fields = (
            'url',
            'pk',
            'almacen',
            'estado',
            'articulo',
            'cantidad',
        )

    def get_estado(self, obj):
        try:
            return obj.get_estado_display()
        except:
            return ""

    def get_almacen(self, obj):

        try:
            return "({}) {}".format(
                obj.almacen.clave,
                obj.almacen.descripcion
            )

        except:
            return ""

    def get_articulo(self, obj):

        try:
            return "({}) {}".format(
                obj.articulo.clave,
                obj.articulo.descripcion
            )

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


class EntradaDetalleSerializer(serializers.HyperlinkedModelSerializer):

    articulo = serializers.SerializerMethodField()
    cabecera = serializers.SerializerMethodField()

    class Meta:
        model = EntradaDetalle
        fields = (
            'url',
            'pk',
            'cantidad',
            'articulo',
            'cabecera',
        )

    def get_articulo(self, obj):

        try:
            return "({}) {}".format(
                obj.articulo.clave.encode("utf-8"),
                obj.articulo.descripcion.encode("utf-8")
            )
        except:
            return ""

    def get_cabecera(self, obj):

        try:
            return "({}) {}".format(
                obj.cabecera.clave.encode("utf-8"),
                obj.cabecera.descripcion.encode("utf-8")
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
