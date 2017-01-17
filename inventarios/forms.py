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
from .models import UdmArticulo
from .models import EntradaCabecera
from .models import EntradaDetalle


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


# ----------------- UDM ODOMETRO ----------------- #

class UdmArticuloForm(ModelForm):

    class Meta:
        model = UdmArticulo
        fields = '__all__'
        widgets = {
            'clave': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
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
            'estado',
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
            'estado',
        ]
        widgets = {
            'clave': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'tipo': Select(attrs={'class': 'form-control'}),
            'udm': Select(attrs={'class': 'form-control'}),
            'clave_jde': TextInput(attrs={'class': 'form-control'}),
            'estado': Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'clave_jde': 'Clave JDE',
        }


# ----------------- STOCK ----------------- #

class StockFilterForm(Form):

    almacen = ChoiceField(
        widget=Select(
            attrs={'class': 'form-control'}
        )
    )

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
        self.fields['almacen'].choices = self.obtener_Almacenes()

    def obtener_Articulos(self):

        articulo = [('', 'Todos'), ]

        registros = Articulo.objects.all()

        for registro in registros:
            articulo.append(
                (
                    registro.id,
                    "({}) {}".format(
                        registro.clave,
                        registro.descripcion
                    )
                )
            )

        return articulo

    def obtener_Almacenes(self):

        articulo = [('', 'Todos'), ]

        registros = Almacen.objects.all()

        for registro in registros:
            articulo.append(
                (
                    registro.id,
                    "({}) {}".format(
                        registro.clave,
                        registro.descripcion
                    )
                )
            )

        return articulo


# ----------------- ENTRADAS ----------------- #

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


class EntradaDetalleForm(ModelForm):

    class Meta:
        model = EntradaDetalle
        fields = [
            'articulo',
            'cantidad',
        ]

        widgets = {
            'articulo': Select(attrs={'class': 'form-control'}),
            'cantidad': TextInput(attrs={'class': 'form-control'}),
        }
