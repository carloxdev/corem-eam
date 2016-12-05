# -*- coding: utf-8 -*-

# Librerias django:
from django.conf.urls import url

# Vistas:
from .views import EquipoListView
from .views import EquipoCreateView
from .views import EquipoUpdateView
from .views import UbicacionCreateView, UbicacionListView, UbicacionDeleteView, UbicacionUpdateView, EquipoTreeListView, obtener_arbol


urlpatterns = [
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
    url(
        r'^ubicaciones/eliminar',
        UbicacionDeleteView.as_view(),
        name='activos.ubicaciones_eliminar'
    ),
    url(
        r'^equipos/api_tree',
        obtener_arbol,
        name='activos.api_tree'
    ),

]
