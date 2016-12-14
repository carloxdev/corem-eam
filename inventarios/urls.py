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


urlpatterns = [


    # ----------------- ALMACEN ----------------- #
    url(
        r'^almacenes/$',
        AlmacenListView.as_view(),
        name='activos.almacenes_lista'
    ),
    url(
        r'^almacenes/nuevo/$',
        AlmacenCreateView.as_view(),
        name='activos.almacenes_nuevo'
    ),
    url(
        r'^almacenes/editar/(?P<pk>.*)/$',
        AlmacenUpdateView.as_view(),
        name='activos.almacenes_editar'
    ),


    # ----------------- ARTICULOS ----------------- #
    url(
        r'^articulos/$',
        ArticuloListView.as_view(),
        name='activos.articulos_lista'
    ),
    url(
        r'^articulos/nuevo/$',
        ArticuloCreateView.as_view(),
        name='activos.articulos_nuevo'
    ),
    url(
        r'^articulos/editar/(?P<pk>.*)/$',
        ArticuloUpdateView.as_view(),
        name='activos.articulos_editar'
    ),
]
