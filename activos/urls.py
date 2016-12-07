# -*- coding: utf-8 -*-

# Librerias django:
from django.conf.urls import url

# Vistas:
from .views import EquipoListView
from .views import EquipoCreateView
from .views import EquipoUpdateView
from .views import EquipoTreeListView
from .views import obtener_arbol
from .views import anexar_texto
from .views import anexos

from .views import UbicacionCreateView
from .views import UbicacionListView
from .views import UbicacionUpdateView


urlpatterns = [


    # ----------------- EQUIPO ----------------- #
    url(
        r'^equipos/$',
        EquipoListView.as_view(),
        name='activos.equipos_lista'
    ),
    url(
        r'^equipos/nuevo/$',
        EquipoCreateView.as_view(),
        name='activos.equipos_nuevo'
    ),
    url(
        r'^equipos/editar/(?P<pk>.*)/$',
        EquipoUpdateView.as_view(),
        name='activos.equipos_editar'
    ),
    url(
        r'equipos/arbol/$',
        EquipoTreeListView.as_view(),
        name='activos.equipos_arbol'
    ),
    url(
        r'^equipos/api_tree',
        obtener_arbol,
        name='activos.api_tree'
    ),

    # ----------------- UBICACION ----------------- #

    url(
        r'ubicaciones/$',
        UbicacionListView.as_view(),
        name='activos.ubicaciones_lista'
    ),
    url(
        r'^ubicaciones/nuevo/$',
        UbicacionCreateView.as_view(),
        name='activos.ubicaciones_nuevo'
    ),
    url(
        r'^ubicaciones/editar/(?P<pk>\d+)',
        UbicacionUpdateView.as_view(),
        name='activos.ubicaciones_editar'
    ),

    # ----------------- ANEXOS ------------------ #

    url(
        r'equipos/anexos/(?P<pk>\d+)/$',
        anexos,
        name="activos.equipos_anexar"
    ),
    url(
        r'equipos/anexos/(?P<pk>\d+)/texto',
        anexar_texto,
        name="activos.anexar_texto"
    ),
]
