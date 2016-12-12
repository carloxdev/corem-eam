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

    def get_Descendencia(self, _hijos):

        for hijo in _hijos:

            nodo = {}
            nodo["text"] = hijo.descripcion
            nodo["href"] = hijo.id,
            nodo["tag"] = ['0']

            # if len(hijo )

    def get_Json(self, _daddies):

        lista = []

        for daddy in _daddies:

            nodo = {}
            nodo["text"] = daddy.descripcion
            nodo["href"] = daddy.id,
            nodo["tag"] = ['0']

            lista.append(nodo)

            hijos = Equipo.objects.filter(padre=daddy)

            if len(hijos):
                self.get_Descendencia(hijos)

        lista_json = json.dumps(lista)

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


# def obtener_arbol(request):
#     tree = {'text': '', 'nodes': []}
#     sub_tree = tree['nodes']

#     def print_Hijos(_hijos, _tag):

#         _tag += "--"

#         for hijo in _hijos:
#             print "{} Hijo: {}".format(_tag, hijo)
#             hijos = Equipo.objects.filter(padre=hijo)
#             if len(hijos) > 0:
#                 print_Hijos(hijos, _tag)

#         return None

#     daddies = Equipo.objects.filter(padre=None)
#     tag = "--"

#     for daddy in daddies:

#         print "Padre: {}".format(daddy)

#         hijos = Equipo.objects.filter(padre=daddy)
#         print_Hijos(hijos, tag)

#     return HttpResponse(json.dumps(tree), content_type="application/json")
