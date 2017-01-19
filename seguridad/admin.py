# -*- coding: utf-8 -*-

# Librerias Django:
from django.contrib import admin

# Modelos:
from .models import Profile


@admin.register(Profile)
class AdminUbicacion(admin.ModelAdmin):
    list_display = (
        'user',
        'puesto',
        'clave',
        'fecha_nacimiento',
        'imagen',
        'comentarios',
    )
