# -*- coding: utf-8 -*-

# Librerias django
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

# API Rest
from rest_framework import routers

# API Rest - Views:
from activos.views import EquipoAPI, UbicacionAPI, TextoEquipoAnexoAPI

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
    r'equipos/anexos/texto',
    TextoEquipoAnexoAPI,
    'equipos_anexos_texto'
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'', include('seguridad.urls')),
    url(r'', include('activos.urls')),
]


if settings.DEBUG:

    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
