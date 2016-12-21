# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas:
from .views import OrdenTrabajoListView
from .views import OrdenTrabajoCreateView

app_name = 'trabajos'
urlpatterns = [

    # ----------------- ORDEN DE TRABAJO ----------------- #
    url(
        r'^ordenes/$',
        OrdenTrabajoListView.as_view(),
        name='ordenes_lista'
    ),

    url(
        r'^ordenes/nuevo/$',
        OrdenTrabajoCreateView.as_view(),
        name='ordenes_nueva'
    ),


]
