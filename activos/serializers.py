# -*- coding: utf-8 -*-

# Librerias Python:
import json

# API REST:
from rest_framework import serializers

# Modelos:
from .models import Equipo
from .models import Ubicacion
from .models import Odometro
from .models import Medicion
from .models import UdmOdometro


# ----------------- EQUIPO ----------------- #

class EquipoSerializer(serializers.HyperlinkedModelSerializer):

    padre = serializers.SerializerMethodField()
    empresa = serializers.SerializerMethodField()
    ubicacion = serializers.SerializerMethodField()

    estado = serializers.SerializerMethodField()

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
            return "({}) {}".format(
                obj.padre.tag,
                obj.padre.descripcion
            )

        except:
            return ""

    def get_empresa(self, obj):

        try:
            return obj.empresa.clave
        except:
            return ""

    def get_ubicacion(self, obj):

        try:
            return "({}) {}".format(
                obj.ubicacion.clave.encode("utf-8"),
                obj.ubicacion.descripcion.encode("utf-8")
            )
        except:
            return ""

    def get_estado(self, obj):
        try:
            return obj.get_estado_display()
        except:
            return ""


class EquipoTreeSerilizado(object):

    def __init__(self):
        self.lista = []

    def get_Descendencia(self, _hijos, _nodo_padre):

        lista_desendencia = []

        for hijo in _hijos:

            nodo = {}
            nodo["text"] = "{} : {}".format(hijo.tag, hijo.descripcion)
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
            # nodo["text"] = daddy.descripcion
            # nodo["href"] = "#{}".format(daddy.id)
            # nodo["tag"] = ['0']
            nodo["icon"] = "fa fa-sitemap"
            hijos = Equipo.objects.filter(padre=daddy)

            if len(hijos):
                nodo["text"] = "Sub-Equipos:"
                nodo["nodes"] = self.get_Descendencia(hijos, nodo)
                nodo["backColor"] = "#307AAE"
                nodo["color"] = "#FFFFFF"
            else:
                nodo["text"] = "Sin Sub-Equipos"
                nodo["backColor"] = "#F2F2F2"
                nodo["color"] = "#000000"

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


# ----------------- UDM ----------------- #

class UdmOdometroSerializer(serializers.ModelSerializer):

    class Meta:
        model = UdmOdometro
        fields = (
            'pk',
            'url',
            'clave',
            'descripcion'
        )


# ----------------- ODOMETRO ------------------ #

class OdometroSerializer(serializers.ModelSerializer):

    equipo = serializers.SerializerMethodField()

    class Meta:
        model = Odometro
        fields = (
            'pk',
            'url',
            'equipo',
            'clave',
            'descripcion',
            'udm',
            'esta_activo',
        )

    def get_equipo(self, obj):

        try:
            return obj.equipo.tag
        except:
            return ""


# ----------------- MEDICION ------------------ #

class MedicionSerializer(serializers.ModelSerializer):

    odometro_clave = serializers.SerializerMethodField()
    equipo = serializers.SerializerMethodField()
    udm = serializers.SerializerMethodField()

    class Meta:
        model = Medicion
        fields = (
            'pk',
            'url',
            'odometro',
            'odometro_clave',
            'equipo',
            'udm',
            'fecha',
            'lectura',
        )

    def get_odometro_clave(self, obj):

        try:
            return obj.odometro.clave
        except:
            return ""

    def get_equipo(self, obj):
        try:
            return obj.odometro.equipo.tag
        except:
            return ""

    def get_udm(self, obj):
        try:
            return obj.odometro.get_udm_display()
        except:
            return ""
