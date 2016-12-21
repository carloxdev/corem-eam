# -*- coding: utf-8 -*-

# Django:
from django.forms import ModelForm
from django.forms import TextInput
from django.forms import Select
from django.forms import CheckboxInput
from django.forms import Textarea


# Modelos:
from .models import OrdenTrabajo


# ----------------- ORDEN DE TRABAJO ----------------- #

class OrdenTrabajoForm(ModelForm):

    class Meta:
        model = OrdenTrabajo
        fields = '__all__'
        widgets = {
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'equipo': Select(attrs={'class': 'form-control select2'}),
            'tipo': Select(attrs={'class': 'form-control select2'}),
            'estado': Select(attrs={'class': 'form-control select2'}),
            'fecha_estimada_inicio': TextInput(
                attrs={'class': 'form-control'}
            ),
            'fecha_estimada_fin': TextInput(attrs={'class': 'form-control'}),
            'fecha_real_inicio': TextInput(attrs={'class': 'form-control'}),
            'fecha_real_fin': TextInput(attrs={'class': 'form-control'}),
            'es_template': CheckboxInput(),


            'responsable': TextInput(attrs={'class': 'form-control select2'}),
            'observaciones': Textarea(attrs={'class': 'form-control'}),



        }
