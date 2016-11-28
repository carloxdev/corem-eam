# -*- coding: utf-8 -*-

# Librerias django:
from django.conf.urls import url

# Vistas:
from .views import EquipoListView
from .views import EquipoCreateView
from .views import EquipoUpdateView

urlpatterns = [
    url(
        r'^equipos/$',
        EquipoListView.as_view(),
        name='activos.equipos'
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
]
