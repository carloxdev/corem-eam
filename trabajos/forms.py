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
from activos.models import Equipo
from .models import OrdenTrabajo
# from .models import ORDEN_TIPO
# from .models import EQUIPO_ESTADO

# ----------------- ORDEN DE TRABAJO ----------------- #


class OrdenTrabajoForm(ModelForm):

    class Meta:
        model = OrdenTrabajo
        fields = '__all__'
        widgets = {
            'descripcion': TextInput(attrs={'class': 'form-control input-sm'}),
            'equipo': Select(attrs={'class': 'form-control input-sm select2'}),
            'tipo': Select(attrs={'class': 'form-control input-sm select2'}),
            'estado': Select(attrs={'class': 'form-control input-sm select2'}),
            'fecha_estimada_inicio': TextInput(
                attrs={
                    'class': 'form-control input-sm',
                    'data-date-format': 'yyyy-mm-dd'
                }
            ),
            'fecha_estimada_fin': TextInput(
                attrs={
                    'class': 'form-control input-sm',
                    'data-date-format': 'yyyy-mm-dd'
                }
            ),
            'fecha_real_inicio': TextInput(
                attrs={
                    'class': 'form-control input-sm',
                    'data-date-format': 'yyyy-mm-dd'
                }
            ),
            'fecha_real_fin': TextInput(
                attrs={
                    'class': 'form-control input-sm',
                    'data-date-format': 'yyyy-mm-dd'
                }
            ),
            'es_template': CheckboxInput(),


            'responsable': TextInput(
                attrs={'class': 'form-control input-sm select2'}
            ),
            'observaciones': Textarea(
                attrs={'class': 'form-control input-sm'}
            ),
        }
        labels = {
            'es_template': "Template"
        }


class OrdenTrabajoFiltersForm(Form):

    tipo = ChoiceField(
        widget=Select(attrs={'class': 'form-control input-sm  select2'})
    )
    estado = ChoiceField(
        widget=Select(
            attrs={'class': 'form-control input-sm  select2'}
        )
    )
    descripcion = CharField(
        widget=TextInput(attrs={'class': 'form-control input-sm'})
    )
    equipo = ChoiceField(
        widget=Select(
            attrs={'class': 'form-control input-sm  select2'}
        )
    )
    responsable = CharField(
        widget=TextInput(attrs={'class': 'form-control input-sm'})
    )

    def __init__(self, *args, **kwargs):

        super(OrdenTrabajoFiltersForm, self).__init__(*args, **kwargs)
        self.fields['equipo'].choices = self.get_Equipos()
        self.fields['tipo'].choices = self.get_Tipos(OrdenTrabajo.ORDEN_TIPO)
        self.fields['estado'].choices = self.get_Estados(
            OrdenTrabajo.ORDEN_ESTADO
        )

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

    def get_Equipos(self):

        equipo = [('', '-------')]

        registros = Equipo.objects.all()

        for registro in registros:
            equipo.append(
                (
                    registro.tag,
                    "{} - {}".format(
                        registro.tag.encode('utf-8'),
                        registro.descripcion.encode('utf-8')
                    )
                )
            )

        return equipo
