# -*- coding: utf-8 -*-

# API REST:
from rest_framework import serializers

# Modelos:
from .models import OrdenTrabajo


# ----------------- ORDEN DE TRABAJO ----------------- #

class OrdenTrabajoSerializer(serializers.HyperlinkedModelSerializer):

    equipo = serializers.SerializerMethodField()

    tipo = serializers.SerializerMethodField()
    estado = serializers.SerializerMethodField()

    class Meta:
        model = OrdenTrabajo
        fields = (
            'url',
            'id',
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
