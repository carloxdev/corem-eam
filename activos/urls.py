# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas:
from .views import EquipoListView
from .views import EquipoCreateView
from .views import EquipoUpdateView
from .views import EquipoTreeListView
from .views import OdometroListView
from .views import OdometroCreateView
from .views import OdometroUpdateView

from .views import EquipoTreeAPI
from .views import AnexoTextoView
from .views import AnexoImagenView
from .views import AnexoArchivoView

from .views import UbicacionCreateView
from .views import UbicacionListView
from .views import UbicacionUpdateView

from .views import UdmOdometroCreateView
from .views import UdmOdometroListView
from .views import UdmOdometroUpdateView

from .views import MedicionCreateView
from .views import MedicionOdometroView


app_name = "activos"

urlpatterns = [

    # ----------------- EQUIPO ----------------- #
    url(
        r'^equipos/$',
        EquipoListView.as_view(),
        name='equipos_lista'
    ),
    url(
        r'^equipos/nuevo/$',
        EquipoCreateView.as_view(),
        name='equipos_nuevo'
    ),
    url(
        r'^equipos/editar/(?P<pk>.*)/$',
        EquipoUpdateView.as_view(),
        name='equipos_editar'
    ),
    url(
        r'equipos/arbol/(?P<pk>\d+)/$',
        EquipoTreeListView.as_view(),
        name='equipos_arbol'
    ),
    url(
        r'^equipos/arbol/json/(?P<pk>\d+)/$',
        EquipoTreeAPI.as_view(),
        name='equipos_api_tree'
    ),

    # ----------------- ANEXOS ------------------ #

    url(
        r'equipos/anexos/(?P<pk>\d+)/texto/$',
        AnexoTextoView.as_view(),
        name='anexar_texto'
    ),
    url(
        r'^equipos/anexos/(?P<pk>\d+)/imagen/$',
        AnexoImagenView.as_view(),
        name='anexar_imagen'
    ),
    url(
        r'^equipos/anexos/(?P<pk>\d+)/archivo/$',
        AnexoArchivoView.as_view(),
        name='anexar_archivo'
    ),

    # ----------------- UBICACION ----------------- #

    url(
        r'ubicaciones/$',
        UbicacionListView.as_view(),
        name='ubicaciones_lista'
    ),
    url(
        r'^ubicaciones/nuevo/$',
        UbicacionCreateView.as_view(),
        name='ubicaciones_nuevo'
    ),
    url(
        r'^ubicaciones/editar/(?P<pk>\d+)/$',
        UbicacionUpdateView.as_view(),
        name='ubicaciones_editar'
    ),


    # ----------------- UDM ODOMETRO ----------------- #

    url(
        r'udms/$',
        UdmOdometroListView.as_view(),
        name='udms_odometro_lista'
    ),
    url(
        r'udms/nuevo/$',
        UdmOdometroCreateView.as_view(),
        name='udms_odometro_nuevo'
    ),
    url(
        r'udms/editar/(?P<pk>\d+)/$',
        UdmOdometroUpdateView.as_view(),
        name='udms_odometro_editar'
    ),

    # ----------------- ODOMETRO ----------------- #
    url(
        r'^odometros/$',
        OdometroListView.as_view(),
        name='odometros_lista'
    ),
    url(
        r'^odometros/nuevo/$',
        OdometroCreateView.as_view(),
        name='odometros_nuevo'
    ),
    url(
        r'^odometros/editar/(?P<pk>.*)/$',
        OdometroUpdateView.as_view(),
        name='odometros_lista'
    ),

    # ----------------- MEDICION ----------------- #

    url(
        r'^mediciones/nuevo',
        MedicionCreateView.as_view(),
        name='mediciones_nuevo'
    ),
    url(
        r'^odometros/(?P<pk>.*)/mediciones/$',
        MedicionOdometroView.as_view(),
        name='odometros_mediciones'
    ),

]
