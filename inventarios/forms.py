# -*- coding: utf-8 -*-

# Django:
from django.forms import ModelForm
from django.forms import TextInput
from django.forms import Select

# Modelos:
from .models import Almacen
from .models import Articulo


# ----------------- ALMACEN ----------------- #

class AlmacenForm(ModelForm):

    class Meta:
        model = Almacen
        fields = [
            # 'empresa',
            'clave',
            'descripcion',
        ]
        widgets = {
            # 'empresa': TextInput(attrs={'class': 'form-control'}),
            'clave': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
        }


# ----------------- ARTICULO ----------------- #

class ArticuloFilterForm(ModelForm):

    class Meta:
        model = Articulo
        fields = [
            'clave_jde',
            'descripcion',
            'tipo',
        ]
        widgets = {
            'clave_jde': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'tipo': Select(attrs={'class': 'form-control'}),
        }


class ArticuloForm(ModelForm):

    class Meta:
        model = Articulo
        fields = [
            'clave_jde',
            'descripcion',
            'tipo',
            'udm',
        ]
        widgets = {
            'clave_jde': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'tipo': Select(attrs={'class': 'form-control'}),
            'udm': Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'clave_jde': 'Clave JDE',
        }
