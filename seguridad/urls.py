# -*- coding: utf-8 -*-

# Librerias django:
from django.conf.urls import url
# from django.contrib.auth import views as auth_views
# from django.conf import settings

# Vistas:
from .views import Dashboard
from .views import Login


urlpatterns = [
    url(r'^dashboard/$', Dashboard.as_view(), name='seguridad.dashboard'),
    url(r'^$', Login.as_view(), name='seguriddad.login'),
]
