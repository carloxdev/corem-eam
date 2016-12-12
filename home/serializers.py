# -*- coding: utf-8 -*-

# API REST:
from rest_framework import serializers

# Modelos:
from .models import AnexoTexto


class AnexoTextoSerializer(serializers.HyperlinkedModelSerializer):

    equipo = serializers.SerializerMethodField()

    class Meta:
        model = AnexoTexto
        fields = (
            'pk',
            'equipo',
            'texto',
        )

    def get_equipo(self, obj):
        try:
            return obj.equipo.tag
        except:
            return ""
