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
from activos.views import AnexoTextoAPI
from activos.views import AnexoArchivoAPI
from activos.views import AnexoImagenAPI
from activos.views import OdometroAPI
from activos.views import MedicionAPI

from inventarios.views import AlmacenAPI
from inventarios.views import ArticuloAPI
from inventarios.views import ArticuloAnexoTextoAPI
from inventarios.views import ArticuloAnexoImagenAPI
from inventarios.views import ArticuloAnexoArchivoAPI

from trabajos.views import OrdenTrabajoAPI
from trabajos.views import OrdenAnexoTextoAPI
from trabajos.views import OrdenAnexoImagenAPI
from trabajos.views import OrdenAnexoArchivoAPI

# Librerias necesarias para publicar Medias en DEBUG
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register(
    r'equipos',
    EquipoAPI,
    'equipo'
)
router.register(
    r'ubicaciones',
    UbicacionAPI,
    'ubicacion'
)
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
router.register(
    r'almacenes',
    AlmacenAPI,
    'almacen'
)
router.register(
    r'articulos',
    ArticuloAPI,
    'articulo'
)
router.register(
    r'ordenestrabajo',
    OrdenTrabajoAPI,
    'ordentrabajo'
)
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
router.register(
    r'odometros',
    OdometroAPI,
    'odometro'
)
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
router.register(
    r'mediciones',
    MedicionAPI,
    'medicion'
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
