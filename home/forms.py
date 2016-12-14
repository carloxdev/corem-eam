# -*- coding: utf-8 -*-

# Django:
from django.forms import ModelForm
from django.forms import TextInput
from django.forms import Textarea

# Modelos:
from .models import AnexoArchivo
from .models import AnexoImagen
from .models import AnexoTexto


class AnexoTextoForm(ModelForm):

    class Meta:
        model = AnexoTexto
        fields = ['texto']
        widgets = {
            'texto': Textarea(attrs={'class': 'textarea form-control'})
        }
        labels = {
            'texto': 'Introduzca texto',
        }


class AnexoImagenForm(ModelForm):

    class Meta:
        model = AnexoImagen
        fields = ['descripcion', 'ruta']
        labels = {
            'ruta': 'Imagen',
            'descripcion': 'Descripción o comentario',
        }
        widgets = {
            'descripcion': TextInput(attrs={'class': 'form-control'})
        }


class AnexoArchivoForm(ModelForm):

    class Meta:
        model = AnexoArchivo
        fields = ['descripcion', 'archivo']
        labels = {
            'descripcion': 'Descripción',
            'archivo': 'Subir archivo',
        }
        widgets = {
            'descripcion': TextInput(attrs={'class': 'form-control'})
        }
