# -*- coding: utf-8 -*-

# Librerias django:
from django.conf.urls import url

# Vistas:
from .views import EquipoListView


urlpatterns = [
    url(r'^equipos/$', EquipoListView.as_view(), name='activos.equipos'),
]
