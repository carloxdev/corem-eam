# -*- coding: utf-8 -*-

# LIBRERIAS Python
import json

# API REST:
from rest_framework import serializers

# Modelos:
from .models import Equipo
from .models import Ubicacion


# ----------------- EQUIPO ----------------- #

class EquipoSerializer(serializers.HyperlinkedModelSerializer):

    padre = serializers.SerializerMethodField()
    empresa = serializers.SerializerMethodField()
    ubicacion = serializers.SerializerMethodField()

    class Meta:
        model = Equipo
        fields = (
            'url',
            'pk',
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


class EquipoTreeSerilizado(object):

    def __init__(self):
        self.lista = []

    def get_Descendencia(self, _hijos, _nodo_padre):

        lista_desendencia = []

        for hijo in _hijos:

            nodo = {}
            nodo["text"] = hijo.descripcion
            # nodo["href"] = "#{}".format(hijo.id)
            # nodo["tag"] = ['0']

            nietos = Equipo.objects.filter(padre=hijo)

            if len(nietos):
                nodo["nodes"] = self.get_Descendencia(nietos, nodo)

            lista_desendencia.append(nodo)

        return lista_desendencia

    def get_Json(self, _daddies):

        self.lista = []

        for daddy in _daddies:

            nodo = {}
            nodo["text"] = daddy.descripcion
            # nodo["href"] = "#{}".format(daddy.id)
            # nodo["tag"] = ['0']

            hijos = Equipo.objects.filter(padre=daddy)

            if len(hijos):
                nodo["nodes"] = self.get_Descendencia(hijos, nodo)

            self.lista.append(nodo)

        lista_json = json.dumps(self.lista)

        return lista_json


# ----------------- UBICACION ----------------- #

class UbicacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ubicacion
        fields = (
            'pk',
            'url',
            'clave',
            'descripcion'
        )
