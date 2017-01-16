# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas:
from .views import AlmacenListView
from .views import AlmacenCreateView
from .views import AlmacenUpdateView

from .views import StockListView

from .views import UdmArticuloListView
from .views import UdmArticuloCreateView
from .views import UdmArticuloUpdateView

from .views import ArticuloListView
from .views import ArticuloCreateView
from .views import ArticuloUpdateView

from .views import ArticuloAnexoTextoView
from .views import ArticuloAnexoImagenView
from .views import ArticuloAnexoArchivoView

from .views import EntradaListView
from .views import EntradaCabeceraCreateView

app_name = "inventarios"

urlpatterns = [

    # ----------------- ALMACEN ----------------- #

    url(
        r'^almacenes/$',
        AlmacenListView.as_view(),
        name='almacenes_lista'
    ),
    url(
        r'^almacenes/nuevo/$',
        AlmacenCreateView.as_view(),
        name='almacenes_nuevo'
    ),
    url(
        r'^almacenes/editar/(?P<pk>.*)/$',
        AlmacenUpdateView.as_view(),
        name='almacenes_editar'
    ),


    # ----------------- UDM ARTICULO ----------------- #

    url(
        r'udmarticulo/$',
        UdmArticuloListView.as_view(),
        name='udms_articulo_lista'
    ),
    url(
        r'udmarticulo/nuevo/$',
        UdmArticuloCreateView.as_view(),
        name='udms_articulo_nuevo'
    ),
    url(
        r'udmarticulo/editar/(?P<pk>\d+)/$',
        UdmArticuloUpdateView.as_view(),
        name='udms_articulo_editar'
    ),



    # ----------------- ARTICULOS ----------------- #

    url(
        r'^articulos/$',
        ArticuloListView.as_view(),
        name='articulos_lista'
    ),
    url(
        r'^articulos/nuevo/$',
        ArticuloCreateView.as_view(),
        name='articulos_nuevo'
    ),
    url(
        r'^articulos/editar/(?P<pk>.*)/$',
        ArticuloUpdateView.as_view(),
        name='articulos_editar'
    ),


    # ----------------- ARTICULOS - ANEXOS ----------------- #

    url(
        r'articulos/anexos/(?P<pk>\d+)/texto/$',
        ArticuloAnexoTextoView.as_view(),
        name='anexar_texto'
    ),
    url(
        r'^articulos/anexos/(?P<pk>\d+)/imagen/$',
        ArticuloAnexoImagenView.as_view(),
        name='anexar_imagen'
    ),
    url(
        r'^articulos/anexos/(?P<pk>\d+)/archivo/$',
        ArticuloAnexoArchivoView.as_view(),
        name='anexar_archivo'
    ),


    # ----------------- STOCK ----------------- #

    url(
        r'^stock/(?P<pk>\d+)/$',
        StockListView.as_view(),
        name='stock_lista'
    ),


    # ----------------- ENTRADAS ----------------- #

    url(
        r'entradas/$',
        EntradaListView.as_view(),
        name='entradas_lista'
    ),
    url(
        r'entradas/nuevo/$',
        EntradaCabeceraCreateView.as_view(),
        name='entradas_nuevo'
    ),
]
