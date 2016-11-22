# -*- coding: utf-8 -*-

# Librerias Django:
from django.contrib import admin

# Modelos:
from .models import Empresa


@admin.register(Empresa)
class AdminEmpresa(admin.ModelAdmin):
    list_display = (
        'clave',
        'descripcion',
        'logo',
    )
