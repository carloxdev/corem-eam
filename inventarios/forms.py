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
from .models import MovimientoCabecera
from .models import MovimientoDetalle


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
            # 'empresa': TextInput(attrs={'class': 'form-control input-sm'}),
            'clave': TextInput(attrs={'class': 'form-control input-sm'}),
            'descripcion': TextInput(attrs={'class': 'form-control input-sm'}),
            'estado': Select(attrs={'class': 'form-control input-sm'}),
        }


# ----------------- UDM ODOMETRO ----------------- #

class UdmArticuloForm(ModelForm):

    class Meta:
        model = UdmArticulo
        fields = '__all__'
        widgets = {
            'clave': TextInput(attrs={'class': 'form-control input-sm'}),
            'descripcion': TextInput(attrs={'class': 'form-control input-sm'}),
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
            'imagen',
        ]
        widgets = {
            'clave': TextInput(attrs={'class': 'form-control input-sm'}),
            'descripcion': TextInput(attrs={'class': 'form-control input-sm'}),
            'tipo': Select(attrs={'class': 'form-control input-sm'}),
            'clave_jde': TextInput(attrs={'class': 'form-control input-sm'}),
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
            'imagen',
        ]
        widgets = {
            'clave': TextInput(attrs={'class': 'form-control input-sm'}),
            'descripcion': TextInput(attrs={'class': 'form-control input-sm'}),
            'tipo': Select(attrs={'class': 'form-control input-sm'}),
            'udm': Select(attrs={'class': 'form-control input-sm'}),
            'clave_jde': TextInput(attrs={'class': 'form-control input-sm'}),
            'estado': Select(attrs={'class': 'form-control input-sm'}),
        }
        labels = {
            'clave_jde': 'Clave JDE',
        }


# ----------------- STOCK ----------------- #

class StockFilterForm(Form):

    almacen = ChoiceField(
        widget=Select(
            attrs={'class': 'form-control input-sm'}
        )
    )

    articulo = ChoiceField(
        widget=Select(
            attrs={'class': 'form-control input-sm'}
        )
    )

    cantidad_menorque = CharField(
        widget=TextInput(
            attrs={'class': 'form-control input-sm'})
    )

    cantidad_mayorque = CharField(
        widget=TextInput(
            attrs={'class': 'form-control input-sm'})
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


# ----------------- MOVIMIENTOS ----------------- #

class MovimientoCabeceraFilterForm(ModelForm):

    class Meta:
        model = MovimientoCabecera
        fields = [
            'descripcion',
            'almacen_origen',
            'almacen_destino',
            'persona_recibe',
            'persona_entrega',
            'estado',
            'tipo',
        ]
        widgets = {
            'descripcion': TextInput(attrs={'class': 'form-control input-sm'}),
            'almacen_origen': Select(attrs={'class': 'form-control input-sm'}),
            'almacen_destino': Select(
                attrs={'class': 'form-control input-sm'}
            ),
            'persona_recibe': TextInput(
                attrs={'class': 'form-control input-sm'}
            ),
            'persona_entrega': TextInput(
                attrs={'class': 'form-control input-sm'}
            ),
            'estado': Select(attrs={'class': 'form-control input-sm'}),
            'tipo': Select(attrs={'class': 'form-control input-sm'}),

        }


class MovimientoCabeceraForm(ModelForm):

    class Meta:
        model = MovimientoCabecera
        fields = [
            'fecha',
            'descripcion',
            'almacen_origen',
            'almacen_destino',
            'persona_recibe',
            'persona_entrega',
        ]
        widgets = {
            'fecha': TextInput(attrs={'class': 'form-control input-sm',
                                      'data-date-format': 'yyyy-mm-dd'}),
            'descripcion': TextInput(attrs={'class': 'form-control input-sm'}),
            'almacen_origen': Select(attrs={'class': 'form-control input-sm'}),
            'almacen_destino': Select(
                attrs={'class': 'form-control input-sm'}
            ),
            'persona_recibe': TextInput(
                attrs={'class': 'form-control input-sm'}
            ),
            'persona_entrega': TextInput(
                attrs={'class': 'form-control input-sm'}
            ),

        }


class MovimientoDetalleForm(ModelForm):

    class Meta:
        model = MovimientoDetalle
        fields = [
            'articulo',
        ]

        widgets = {
            'articulo': Select(attrs={'class': 'form-control input-sm'}),
        }


class EntradaSaldoForm(ModelForm):

    class Meta:
        model = MovimientoCabecera
        fields = [
            'descripcion',
            'almacen_destino',
            'fecha',
        ]
        widgets = {
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'almacen_destino': Select(attrs={'class': 'form-control'}),
            'fecha': TextInput(attrs={'class': 'form-control',
                                      'data-date-format': 'yyyy-mm-dd'}),
        }


class EntradaCompraForm(ModelForm):

    class Meta:
        model = MovimientoCabecera
        fields = [
            'descripcion',
            'fecha',
            'almacen_destino',
            'persona_entrega',
            'persona_recibe',
        ]
        widgets = {
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'almacen_destino': Select(attrs={'class': 'form-control'}),
            'fecha': TextInput(attrs={'class': 'form-control',
                                      'data-date-format': 'yyyy-mm-dd'}),
            'persona_entrega': TextInput(attrs={'class': 'form-control'}),
            'persona_recibe': TextInput(attrs={'class': 'form-control'}),
        }