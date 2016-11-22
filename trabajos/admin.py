# -*- coding: utf-8 -*-

# Librerias django
from django.contrib import admin

# Modelos:
from .models import OrdenTrabajo


@admin.register(OrdenTrabajo)
class AdminOrdenTrabajo(admin.ModelAdmin):
	list_display = (
		'empresa',
		'equipo',
		'descripcion',
		'tipo',
		'estado',
		'fecha_estimada_inicio',
		'fecha_estimada_fin',
		'fecha_real_inicio',
		'fecha_real_fin',
		'es_template',
	)










