# -*- coding: utf-8 -*-

# Django:
from django.forms import ModelForm
from django.forms import Form
from django.forms import TextInput
from django.forms import Select
from django.forms import CheckboxInput
from django.forms import Textarea
from django.forms import ChoiceField
from django.forms import CharField


# Modelos:
from .models import OrdenTrabajo


# ----------------- ORDEN DE TRABAJO ----------------- #
ORDEN_TIPO = (
    ('PREVE', 'PREVENTIVA'),
    ('PREDI', 'PREDICTIVA'),
    ('CORRE', 'CORRECTIVA'),
)

EQUIPO_ESTADO = (
    ('CAP', 'CAPTURA'),
    ('TER', 'TERMINADA'),
    ('CER', 'CERRADA'),
)


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
            'observaciones': Textarea(
                attrs={'class': 'form-control'}
            ),
        }
        labels = {
            'es_template': "Template"
        }


class OrdenTrabajoFiltersForm(Form):

    tipo = ChoiceField(widget=Select(attrs={'class': 'form-control'}))
    estado = ChoiceField(widget=Select(attrs={'class': 'form-control'}))
    descripcion = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    equipo = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    responsable = CharField(widget=TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(OrdenTrabajoFiltersForm, self).__init__(*args, **kwargs)
        self.fields['tipo'].choices = self.get_Tipos(ORDEN_TIPO)
        self.fields['estado'].choices = self.get_Estados(EQUIPO_ESTADO)

    def get_Tipos(self, _opciones):
        opciones = [('', '-------')]

        for registro in _opciones:
            opciones.append(registro)
        return opciones

    def get_Estados(self, _opciones):
        opciones = [('', '-------')]

        for registro in _opciones:
            opciones.append(registro)
        return opciones
