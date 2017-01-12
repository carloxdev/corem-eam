# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas:
from .views import AlmacenListView
from .views import AlmacenCreateView
from .views import AlmacenUpdateView

from .views import ArticuloListView
from .views import ArticuloCreateView
from .views import ArticuloUpdateView

from .views import ArticuloAnexoTextoView
from .views import ArticuloAnexoImagenView
from .views import ArticuloAnexoArchivoView

from .views import EntradaCabeceraListView
from .views import EntradaCabeceraCreateView


urlpatterns = [


    # ----------------- ALMACEN ----------------- #
    url(
        r'^almacenes/$',
        AlmacenListView.as_view(),
        name='inventarios.almacenes_lista'
    ),
    url(
        r'^almacenes/nuevo/$',
        AlmacenCreateView.as_view(),
        name='inventarios.almacenes_nuevo'
    ),
    url(
        r'^almacenes/editar/(?P<pk>.*)/$',
        AlmacenUpdateView.as_view(),
        name='inventarios.almacenes_editar'
    ),


    # ----------------- ARTICULOS ----------------- #
    url(
        r'^articulos/$',
        ArticuloListView.as_view(),
        name='inventarios.articulos_lista'
    ),
    url(
        r'^articulos/nuevo/$',
        ArticuloCreateView.as_view(),
        name='inventarios.articulos_nuevo'
    ),
    url(
        r'^articulos/editar/(?P<pk>.*)/$',
        ArticuloUpdateView.as_view(),
        name='inventarios.articulos_editar'
    ),

    # ----------------- ARTICULOS - ANEXOS ----------------- #
    url(
        r'articulos/anexos/(?P<pk>\d+)/texto/$',
        ArticuloAnexoTextoView.as_view(),
        name='activos.anexar_texto'
    ),
    url(
        r'^articulos/anexos/(?P<pk>\d+)/imagen/$',
        ArticuloAnexoImagenView.as_view(),
        name='activos.anexar_imagen'
    ),
    url(
        r'^articulos/anexos/(?P<pk>\d+)/archivo/$',
        ArticuloAnexoArchivoView.as_view(),
        name='activos.anexar_archivo'
    ),

    # ----------------- ENTRADAS ----------------- #
    url(
        r'entradas/$',
        EntradaCabeceraListView.as_view(),
        name='inventarios.entradas_lista'
    ),
    url(
        r'entradas/nuevo/$',
        EntradaCabeceraCreateView.as_view(),
        name='inventarios.entradas_nuevo'
    ),
]
