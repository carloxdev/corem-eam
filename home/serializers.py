# -*- coding: utf-8 -*-

# API REST:
from rest_framework import serializers
# Modelos:
from .models import AnexoTexto
from .models import AnexoArchivo
from .models import AnexoImagen


class AnexoTextoSerializer(serializers.HyperlinkedModelSerializer):

    equipo = serializers.SerializerMethodField()

    class Meta:
        model = AnexoTexto
        fields = (
            'url',
            'pk',
            'equipo',
            'texto',
        )

    def get_equipo(self, obj):
        try:
            return obj.equipo.tag
        except:
            return ""


class AnexoArchivoSerializer(serializers.HyperlinkedModelSerializer):

    equipo = serializers.SerializerMethodField()

    class Meta:
        model = AnexoArchivo
        fields = (
            'url',
            'pk',
            'equipo',
            'archivo',
            'descripcion',
        )

    def get_equipo(self, obj):
        try:
            return obj.equipo.tag
        except:
            return ""


class AnexoImagenSerializer(serializers.HyperlinkedModelSerializer):

    equipo = serializers.SerializerMethodField()

    class Meta:
        model = AnexoImagen
        fields = (
            'url',
            'pk',
            'equipo',
            'ruta',
            'descripcion',
        )

    def get_equipo(self, obj):
        try:
            return obj.equipo.tag
        except:
            return ""
