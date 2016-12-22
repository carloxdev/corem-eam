# -*- coding: utf-8 -*-

# Django Atajos:
from django.shortcuts import render

# Django Urls:
from django.core.urlresolvers import reverse_lazy

# Django Generic Views
from django.views.generic.base import View
from django.views.generic import CreateView

# Modelos:
from .models import OrdenTrabajo

# Formularios:
from .forms import OrdenTrabajoForm

# API Rest:
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

# API Rest - Serializadores:
from .serializers import OrdenTrabajoSerializer

# API Rest - Paginacion:
from .pagination import GenericPagination

# API Rest - Filtros:
from .filters import OrdenTrabajoFilter


# ----------------- ORDEN DE TRABAJO ----------------- #


class OrdenTrabajoListView(View):

    def __init__(self):
        self.template_name = 'orden_trabajo/lista.html'

    def get(self, _request):

        return render(_request, self.template_name, {})


class OrdenTrabajoCreateView(CreateView):
    model = OrdenTrabajo
    form_class = OrdenTrabajoForm
    template_name = 'orden_trabajo/formulario.html'
    success_url = reverse_lazy('trabajos:ordenes_lista')

    def get_context_data(self, **kwargs):
        context = super(
            OrdenTrabajoCreateView,
            self
        ).get_context_data(**kwargs)

        data = {
            'operation': "Nuevo"
        }

        context.update(data)

        return context


class OrdenTrabajoAPI(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    pagination_class = GenericPagination

    filter_backends = (DjangoFilterBackend,)
    filter_class = OrdenTrabajoFilter
