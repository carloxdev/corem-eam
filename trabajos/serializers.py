# -*- coding: utf-8 -*-

# API REST:
from rest_framework import serializers

# Modelos:
from .models import OrdenTrabajo
from .models import Actividad
from .models import ManoObra
from .models import Material
from .models import ServicioExterno


# ----------------- ORDEN DE TRABAJO ----------------- #

class OrdenTrabajoSerializer(serializers.HyperlinkedModelSerializer):

    equipo = serializers.SerializerMethodField()

    tipo = serializers.SerializerMethodField()
    estado = serializers.SerializerMethodField()

    class Meta:
        model = OrdenTrabajo
        fields = (
            'url',
            'pk',
            'equipo',
            'descripcion',
            'tipo',
            'estado',
            'responsable',
            'fecha_estimada_inicio',
            'fecha_estimada_fin',
            'fecha_real_inicio',
            'fecha_real_fin',
            'observaciones',
            'es_template',
        )

    def get_equipo(self, obj):

        try:
            return "{} - {}".format(
                obj.equipo.tag,
                obj.equipo.descripcion
            )
        except:
            return ""

    def get_tipo(self, obj):
        try:
            return obj.get_tipo_display()
        except:
            return ""

    def get_estado(self, obj):
        try:
            return obj.get_estado_display()
        except:
            return ""


class ActividadSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Actividad
        fields = (
            'pk',
            'url',
            'orden',
            'numero',
            'descripcion',
            'horas_estimadas',
            'horas_reales',
        )


class MaterialSerializer(serializers.HyperlinkedModelSerializer):

    articulo_id = serializers.SerializerMethodField()
    articulo_desc = serializers.SerializerMethodField()

    class Meta:
        model = Material
        fields = (
            'pk',
            'url',
            'orden',
            'articulo',
            'articulo_id',
            'articulo_desc',
            'cantidad_estimada',
            'cantidad_real',
        )

    def get_articulo_id(self, obj):

        try:
            return obj.articulo.id

        except:
            return 0

    def get_articulo_desc(self, obj):

        try:
            return "({}) {}".format(
                obj.articulo.clave,
                obj.articulo.descripcion
            )

        except:
            return ""


class ManoObraSerializer(serializers.HyperlinkedModelSerializer):

    empleado_id = serializers.SerializerMethodField()
    empleado_desc = serializers.SerializerMethodField()

    class Meta:
        model = ManoObra
        fields = (
            'pk',
            'url',
            'orden',
            'empleado',
            'empleado_id',
            'empleado_desc',
            'descripcion',
            'fecha_inicio',
            'fecha_fin',
            'horas_estimadas',
            'horas_reales',
        )

    def get_empleado_id(self, obj):

        try:
            return obj.empleado.id

        except:
            return 0

    def get_empleado_desc(self, obj):

        try:
            return "({}) {}".format(
                obj.empleado.username,
                obj.empleado.get_full_name()
            )

        except:
            return ""


class ServicioExternoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ServicioExterno
        fields = (
            'pk',
            'url',
            'orden',
            'clave_jde',
            'descripcion',
            'comentarios',
        )
