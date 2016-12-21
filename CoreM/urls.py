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
from inventarios.views import AlmacenAPI
from inventarios.views import ArticuloAPI

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
