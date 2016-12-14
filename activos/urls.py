# -*- coding: utf-8 -*-

# Librerias django:
from django.conf.urls import url

# Vistas:
from .views import EquipoListView
from .views import EquipoCreateView
from .views import EquipoUpdateView
from .views import EquipoTreeListView

from .views import EquipoTreeAPI
from .views import AnexoTextoView
from .views import AnexoImagenView
from .views import AnexoArchivoView

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
        r'equipos/arbol/(?P<pk>\d+)/$',
        EquipoTreeListView.as_view(),
        name='activos.equipos_arbol'
    ),
    url(
        r'^equipos/arbol/json/(?P<pk>\d+)/$',
        EquipoTreeAPI.as_view(),
        name='activos.equipos_api_tree'
    ),

    # ----------------- ANEXOS ------------------ #

    url(
        r'equipos/anexos/(?P<pk>\d+)/texto/$',
        AnexoTextoView.as_view(),
        name='activos.anexar_texto'
    ),
    url(
        r'^equipos/anexos/(?P<pk>\d+)/imagen/$',
        AnexoImagenView.as_view(),
        name='activos.anexar_imagen'
    ),
    url(
        r'^equipos/anexos/(?P<pk>\d+)/archivo/$',
        AnexoArchivoView.as_view(),
        name='activos.anexar_archivo'
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
        r'^ubicaciones/editar/(?P<pk>\d+)/$',
        UbicacionUpdateView.as_view(),
        name='activos.ubicaciones_editar'
    ),

]
