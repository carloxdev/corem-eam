# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas:
from .views import OrdenTrabajoListView
from .views import OrdenTrabajoCreateView
from .views import OrdenTrabajoUpdateView

from .views import ActividadListView
from .views import MaterialListView
from .views import ManoObraListView
from .views import ServicioExternoListView

from .views import OrdenAnexoTextoView
from .views import OrdenAnexoImagenView
from .views import OrdenAnexoArchivoView

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
    url(
        r'^ordenes/editar/(?P<pk>.*)/$',
        OrdenTrabajoUpdateView.as_view(),
        name='ordenes_editar'
    ),

    # ----------------- ACTIVIDADES ----------------- #

    url(
        r'^ordenes/(?P<pk>.*)/actividades/$',
        ActividadListView.as_view(),
        name='actividades_lista'
    ),

    # ----------------- MATERIAL ----------------- #

    url(
        r'^ordenes/(?P<pk>.*)/materiales/$',
        MaterialListView.as_view(),
        name='material_lista'
    ),

    # ----------------- MANO OBRA ----------------- #

    url(
        r'^ordenes/(?P<pk>.*)/mano_obra/$',
        ManoObraListView.as_view(),
        name='mano_obra_lista'
    ),

    # ----------------- SERVICIO EXTERNO ----------------- #

    url(
        r'^ordenes/(?P<pk>.*)/servicios/$',
        ServicioExternoListView.as_view(),
        name='servicio_externo_lista'
    ),

    # ----------------- ORDENES - ANEXOS ----------------- #
    url(
        r'ordenes/anexos/(?P<pk>\d+)/texto/$',
        OrdenAnexoTextoView.as_view(),
        name='orden_anexar_texto'
    ),
    url(
        r'^ordenes/anexos/(?P<pk>\d+)/imagen/$',
        OrdenAnexoImagenView.as_view(),
        name='orden_anexar_imagen'
    ),
    url(
        r'^ordenes/anexos/(?P<pk>\d+)/archivo/$',
        OrdenAnexoArchivoView.as_view(),
        name='orden_anexar_archivo'
    ),


]
