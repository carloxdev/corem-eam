# -*- coding: utf-8 -*-

# Django:
from django import forms
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
        fields = ['titulo', 'texto']
        widgets = {
            'titulo': TextInput(attrs={'class': 'form-control'}),
            'texto': Textarea(attrs={'class': 'textarea form-control'})
        }
        labels = {
            'titulo': 'Título',
            'texto': 'Texto',
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

    # def get_Imagen(self):
    #     datos_formulario = self.cleaned_data
    #     imagen = datos_formulario.get('ruta')

    #     if (imagen is None):
    #         raise forms.ValidationError("Debe seleccionar una imagen")

    #     else:
    #         return imagen

    # def get_Descripcion(self):
    #     datos_formulario = self.cleaned_data
    #     descripcion = datos_formulario.get('descripcion')

    #     if len(descripcion) > 10:
    #         raise forms.ValidationError("Descripción demasiado larga")

    #     else:
    #         return descripcion


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
