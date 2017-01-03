# -*- coding: utf-8 -*-

# Django:
from django.forms import ModelForm
from django.forms import TextInput
from django.forms import Select
from django.forms import CheckboxInput
# Modelos:
from .models import Equipo
from .models import Odometro
from .models import Medicion
from .models import Ubicacion


# ----------------- EQUIPO ----------------- #

class EquipoFiltersForm(ModelForm):

    # def __init__(self, *args, **kwargs):
    #     self.usuario = kwargs.pop('username')
    #     super(EmpresaCreateForm, self).__init__(*args, **kwargs)

    #     if self.usuario.username != 'root':
    #         del self.fields['usuario']

    class Meta:
        model = Equipo
        fields = [
            'tag',
            'descripcion',
            'serie',
            'estado',
            'empresa',
            'padre',
            'sistema',
            'ubicacion',
        ]
        widgets = {
            'tag': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'serie': TextInput(attrs={'class': 'form-control'}),
            'estado': Select(attrs={'class': 'form-control select2'}),
            'empresa': Select(attrs={'class': 'form-control'}),
            'padre': Select(attrs={'class': 'form-control select2'}),
            'sistema': TextInput(attrs={'class': 'form-control'}),
            'ubicacion': Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'tag': 'Tag',
            'descripcion': 'Descripción',
            'serie': 'Serie',
            'estado': 'Estado',
            'padre': 'Padre',
            'empresa': 'Empresa',
            'sistema': 'Sistema',
            'ubicacion': 'Ubicación',
        }


class EquipoForm(ModelForm):

    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'tag': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'serie': TextInput(attrs={'class': 'form-control'}),
            'tipo': TextInput(attrs={'class': 'form-control'}),
            'estado': Select(attrs={'class': 'form-control'}),
            'padre': Select(attrs={'class': 'form-control'}),
            'empresa': Select(attrs={'class': 'form-control'}),
            'sistema': TextInput(attrs={'class': 'form-control'}),
            'ubicacion': Select(attrs={'class': 'form-control'}),
            'cliente': TextInput(attrs={'class': 'form-control'}),
            'responsable': TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'tag': 'Tag',
            'descripcion': 'Descripción',
            'serie': 'Serie',
            'tipo': 'Tipo',
            'estado': 'Estado',
            'padre': 'Padre',
            'empresa': 'Empresa',
            'sistema': 'Sistema',
            'ubicacion': 'Ubicación',
            'imagen': 'Imagen',
            'cliente': 'Cliente',
            'responsable': 'Responsable',
        }

# ----------------- ODÓMETRO ----------------- #


class OdometroForm(ModelForm):

    class Meta:
        model = Odometro
        fields = [
            'equipo',
            'clave',
            'descripcion',
            'udm',
            'esta_activo',
        ]
        widgets = {
            'equipo': Select(attrs={'class': 'form-control'}),
            'clave': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'udm': Select(attrs={'class': 'form-control'}),
            'esta_activo': CheckboxInput(),
        }
        labels = {
            'equipo': 'Equipo',
            'clave': 'Clave',
            'descripcion': 'Descripción',
            'udm': 'UDM',
            'esta_activo': 'Activo',
        }


class OdometroFiltersForm(ModelForm):

    class Meta:
        model = Odometro
        fields = [
            'equipo',
            'clave',
            'descripcion',
            'udm',
        ]
        widgets = {
            'equipo': Select(attrs={'class': 'form-control'}),
            'clave': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'udm': Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'equipo': 'Equipo',
            'clave': 'Clave',
            'descripcion': 'Descripción',
            'udm': 'UDM',
        }

# ----------------- MEDICION ----------------- #


class MedicionFiltersForm(ModelForm):

    class Meta:
        model = Medicion
        fields = [
            'odometro',
        ]
        widgets = {
            'odometro': Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'odometro': 'Odómetro',
        }


class MedicionForm(ModelForm):

    class Meta:
        model = Medicion
        fields = [
            'odometro',
            'fecha',
            'lectura'
        ]
        widgets = {
            'odometro': Select(attrs={'class': 'form-control'}),
            'fecha': TextInput(attrs={'class': 'form-control'}),
            'lectura': TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'odometro': 'Odometro',
            'fecha': 'Fecha',
            'lectura': 'Lectura',
        }

# ----------------- UBICACION ----------------- #


class UbicacionForm(ModelForm):

    class Meta:
        model = Ubicacion
        fields = '__all__'
        widgets = {
            'clave': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
        }
