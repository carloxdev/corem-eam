# -*- coding: utf-8 -*-

# Django:
from django.forms import ModelForm
from django.forms import TextInput
from django.forms import Select
from django.forms import ChoiceField
from django.forms import CharField
from django.forms import Form


# Modelos:
from .models import Almacen
from .models import Articulo
from .models import EntradaCabecera


# ----------------- ALMACEN ----------------- #

class AlmacenForm(ModelForm):

    class Meta:
        model = Almacen
        fields = [
            # 'empresa',
            'clave',
            'descripcion',
            'estado',
        ]
        widgets = {
            # 'empresa': TextInput(attrs={'class': 'form-control'}),
            'clave': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'estado': Select(attrs={'class': 'form-control'}),
        }


# ----------------- ARTICULO ----------------- #

class ArticuloFilterForm(ModelForm):

    class Meta:
        model = Articulo
        fields = [
            'clave',
            'descripcion',
            'tipo',
            'clave_jde',
        ]
        widgets = {
            'clave': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'tipo': Select(attrs={'class': 'form-control'}),
            'clave_jde': TextInput(attrs={'class': 'form-control'}),
        }


class ArticuloForm(ModelForm):

    class Meta:
        model = Articulo
        fields = [
            'clave',
            'descripcion',
            'tipo',
            'udm',
            'clave_jde',
        ]
        widgets = {
            'clave': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'tipo': Select(attrs={'class': 'form-control'}),
            'udm': Select(attrs={'class': 'form-control'}),
            'clave_jde': TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'clave_jde': 'Clave JDE',
        }


# ----------------- STOCK ----------------- #

class StockFilterForm(Form):

    articulo = ChoiceField(
        widget=Select(
            attrs={'class': 'form-control'}
        )
    )

    cantidad_menorque = CharField(
        widget=TextInput(
            attrs={'class': 'form-control'})
    )

    cantidad_mayorque = CharField(
        widget=TextInput(
            attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super(StockFilterForm, self).__init__(*args, **kwargs)
        self.fields['articulo'].choices = self.obtener_Articulos()

    def obtener_Articulos(self):

        articulo = [('', 'Todos'), ]

        registros = Articulo.objects.all()

        for registro in registros:
            articulo.append(
                (
                    registro.clave,
                    "{} - {}".format(
                        registro.clave,
                        registro.descripcion
                    )
                )
            )

        return articulo


# ----------------- ARTICULO ----------------- #

class EntradaCabeceraFilterForm(ModelForm):

    class Meta:
        model = EntradaCabecera
        fields = [
            'clave',
            'descripcion',
            'almacen',
        ]
        widgets = {
            'clave': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'almacen': Select(attrs={'class': 'form-control'}),

        }


class EntradaCabeceraForm(ModelForm):

    class Meta:
        model = EntradaCabecera
        fields = [
            'clave',
            'fecha',
            'descripcion',
            'almacen',
        ]
        widgets = {
            'clave': TextInput(attrs={'class': 'form-control'}),
            'fecha': TextInput(attrs={'class': 'form-control',
                                      'data-date-format': 'yyyy-mm-dd'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'almacen': Select(attrs={'class': 'form-control'}),

        }
