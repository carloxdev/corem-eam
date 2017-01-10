# -*- coding: utf-8 -*-

# Librerias django
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

# API Rest
from rest_framework import routers

# API Rest - Views:
from activos.views import EquipoAPI
from activos.views import UbicacionAPI
from activos.views import UbicacionAPI2
from activos.views import AnexoTextoAPI
from activos.views import AnexoArchivoAPI
from activos.views import AnexoImagenAPI
from activos.views import OdometroAPI
from activos.views import UdmOdometroAPI
from activos.views import UdmOdometroAPI2
from activos.views import MedicionAPI

from inventarios.views import AlmacenAPI
from inventarios.views import ArticuloAPI
from inventarios.views import ArticuloAnexoTextoAPI
from inventarios.views import ArticuloAnexoImagenAPI
from inventarios.views import ArticuloAnexoArchivoAPI
from inventarios.views import EntradaAPI

from trabajos.views import OrdenTrabajoAPI
from trabajos.views import OrdenAnexoTextoAPI
from trabajos.views import OrdenAnexoImagenAPI
from trabajos.views import OrdenAnexoArchivoAPI

# Librerias necesarias para publicar Medias en DEBUG
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()


# ----------------- EQUIPOS ----------------- #

router.register(
    r'equipos',
    EquipoAPI,
    'equipo'
)


# ----------------- EQUIPOS - ANEXOS ----------------- #

router.register(
    r'anexostexto',
    AnexoTextoAPI,
    'anexotexto'
)
router.register(
    r'anexosarchivo',
    AnexoArchivoAPI,
    'anexoarchivo'
),
router.register(
    r'anexosimagen',
    AnexoImagenAPI,
    'anexoimagen'
)

# ----------------- UBICACIONES ----------------- #

router.register(
    r'ubicaciones',
    UbicacionAPI,
    'ubicacion'
)
router.register(
    r'ubicaciones2',
    UbicacionAPI2,
    'ubicacion2'
)


# ----------------- ODOMETROS ----------------- #

router.register(
    r'odometros',
    OdometroAPI,
    'odometro'
)

# ----------------- UDMS - ODOMETRO ----------------- #

router.register(
    r'udmodometro',
    UdmOdometroAPI,
    'udmodometro'
)
router.register(
    r'udmodometro2',
    UdmOdometroAPI2,
    'udmodometro'
)


# ----------------- MEDICIONES ----------------- #

router.register(
    r'mediciones',
    MedicionAPI,
    'medicion'
)


# ----------------- ALMACENES ----------------- #

router.register(
    r'almacenes',
    AlmacenAPI,
    'almacen'
)


# ----------------- ARTICULOS ----------------- #

router.register(
    r'articulos',
    ArticuloAPI,
    'articulo'
)


# ----------------- ARTICULOS - ANEXOS ----------------- #

router.register(
    r'articulosanexotexto',
    ArticuloAnexoTextoAPI,
    'articuloanexotexto'
)
router.register(
    r'articulosanexoimagen',
    ArticuloAnexoImagenAPI,
    'articuloanexoimagen'
)
router.register(
    r'articulosanexoarchivo',
    ArticuloAnexoArchivoAPI,
    'articuloanexoarchivo'
)


# ----------------- ORDENES DE TRABAJO ----------------- #

router.register(
    r'ordenestrabajo',
    OrdenTrabajoAPI,
    'ordentrabajo'
)

# ----------------- ORDENES DE TRABAJO - ANEXOS ----------------- #

router.register(
    r'ordenesanexotexto',
    OrdenAnexoTextoAPI,
    'ordenanexotexto'
)
router.register(
    r'ordenesanexoimagen',
    OrdenAnexoImagenAPI,
    'ordenanexoimagen'
)
router.register(
    r'ordenesanexoarchivo',
    OrdenAnexoArchivoAPI,
    'ordenanexoarchivo'
)

# ----------------- ENTRADAS  ----------------- #

router.register(
    r'entradas',
    EntradaAPI,
    'entradacabecera'
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'', include('seguridad.urls')),
    url(r'', include('activos.urls')),
    url(r'', include('inventarios.urls')),
    url(r'', include('trabajos.urls')),
]


if settings.DEBUG:

    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
