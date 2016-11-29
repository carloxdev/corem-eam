# -*- coding: utf-8 -*-

# Django:
from django.forms import ModelForm
from django.forms import TextInput
from django.forms import Select

# Modelos:
from .models import Equipo, Ubicacion


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
            'estado': TextInput(attrs={'class': 'form-control'}),
            'empresa': Select(attrs={'class': 'form-control'}),
            'padre': Select(attrs={'class': 'form-control select2'}),
            'sistema': TextInput(attrs={'class': 'form-control'}),
            'ubicacion': Select(attrs={'class': 'form-control'}),
        }


class EquipoCreateForm(ModelForm):

    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'tag': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'serie': TextInput(attrs={'class': 'form-control'}),
            'tipo': Select(attrs={'class': 'form-control'}),
            'estado': TextInput(attrs={'class': 'form-control'}),
            'padre': Select(attrs={'class': 'form-control select2'}),
            'empresa': Select(attrs={'class': 'form-control'}),
            'sistema': TextInput(attrs={'class': 'form-control'}),
            'ubicacion': Select(attrs={'class': 'form-control'}),
            
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
            'imagen': 'Imagen'
        }


class EquipoUpdateForm(ModelForm):

    class Meta:
        model = Equipo
        fields = '__all__'
        exclude = ['tag']
        widgets = {
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'serie': TextInput(attrs={'class': 'form-control'}),
            'tipo': Select(attrs={'class': 'form-control'}),
            'estado': TextInput(attrs={'class': 'form-control'}),
            'padre': Select(attrs={'class': 'form-control select2'}),
            'empresa': Select(attrs={'class': 'form-control'}),
            'sistema': TextInput(attrs={'class': 'form-control'}),
            'ubicacion': Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'descripcion': 'Descripción',
            'serie': 'Serie',
            'tipo': 'Tipo',
            'estado': 'Estado',
            'padre': 'Padre',
            'empresa': 'Empresa',
            'sistema': 'Sistema',
            'ubicacion': 'Ubicación',
        }


class UbicacionCreateForm(ModelForm):

    class Meta:
        model = Ubicacion
        fields = '__all__'
        widgets = {
            'clave': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
        }


class UbicacionFiltersForm(ModelForm):

    class Meta:
        model = Ubicacion
        fields = ['descripcion']
        widgets = {
        'descripcion': TextInput(attrs={'class': 'form-control'})
        }
