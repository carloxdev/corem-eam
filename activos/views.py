# -*- coding: utf-8 -*-

# Librerias django

# Django Atajos
from django.shortcuts import render
# from django.shortcuts import redirect

# Django Urls:
# from django.core.urlresolvers import reverse

# Django Generic Views
from django.views.generic.base import View

# Modelos:
from .models import Equipo

# API Rest:
from rest_framework import viewsets

# API Rest - Serializadores:
from .serializers import EquipoSerializer

# API Rest - Paginacion:
from .pagination import GenericPagination

# Formularios:
from forms import EquipoFiltersForm


# ----------------- EMPRESA ----------------- #

class EquipoListView(View):

    def __init__(self):
        self.template_name = 'equipo/lista.html'

    def get(self, request):

        formulario = EquipoFiltersForm()

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)

    def post(self, request):
        return render(request, self.template_name, {})


class EquipoAPI(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    pagination_class = GenericPagination
