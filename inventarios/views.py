# -*- coding: utf-8 -*-

# LIBRERIAS Django

# Django Atajos:
from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# from django.shortcuts import redirect

# Django Urls:
# from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
# from django.http import HttpResponse

# Django Generic Views
from django.views.generic.base import View
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import TemplateView

# Modelos:
# from .models import Udm
from .models import Articulo
from .models import Almacen
# from .models import Stock

# Formularios:
from forms import AlmacenForm
from forms import ArticuloFilterForm
from forms import ArticuloForm

# API Rest:
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# API Rest - Serializadores:
from .serializers import AlmacenSerializer
from .serializers import ArticuloSerializer

# API Rest - Paginacion:
from .pagination import GenericPagination

# API Rest - Filtros:
from .filters import ArticuloFilter

# ----------------- ALMACEN ----------------- #


class AlmacenListView(TemplateView):
    template_name = 'almacen/lista.html'


class AlmacenCreateView(CreateView):
    model = Almacen
    form_class = AlmacenForm
    template_name = 'almacen/formulario.html'
    success_url = reverse_lazy('inventarios.almacenes_lista')

    def get_context_data(self, **kwargs):
        context = super(AlmacenCreateView, self).get_context_data(**kwargs)

        data = {
            'operation': "Nuevo"
        }

        context.update(data)

        return context


class AlmacenUpdateView(UpdateView):
    model = Almacen
    form_class = AlmacenForm
    template_name = 'almacen/formulario.html'
    success_url = reverse_lazy('inventarios.almacenes_lista')

    def get_context_data(self, **kwargs):
        context = super(AlmacenUpdateView, self).get_context_data(**kwargs)

        data = {
            'operation': "Editar"
        }

        context.update(data)

        return context


class AlmacenAPI(viewsets.ModelViewSet):
    queryset = Almacen.objects.all()
    serializer_class = AlmacenSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('clave', 'descripcion',)


# ----------------- ARTICULOS ----------------- #


class ArticuloListView(View):
    def __init__(self):
        self.template_name = 'articulo/lista.html'

    def get(self, request):

        formulario = ArticuloFilterForm()

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)

    def post(self, request):
        return render(request, self.template_name, {})


class ArticuloCreateView(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo/formulario.html'
    success_url = reverse_lazy('inventarios.articulos_lista')

    def get_context_data(self, **kwargs):
        context = super(ArticuloCreateView, self).get_context_data(**kwargs)

        data = {
            'operation': "Nuevo"
        }

        context.update(data)

        return context


class ArticuloUpdateView(UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'almacen/formulario.html'
    success_url = reverse_lazy('inventarios.articulos_lista')

    def get_context_data(self, **kwargs):
        context = super(ArticuloUpdateView, self).get_context_data(**kwargs)

        data = {
            'operation': "Nuevo"
        }

        context.update(data)

        return context


class ArticuloAPI(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    pagination_class = GenericPagination

    filter_backends = (DjangoFilterBackend,)
    filter_class = ArticuloFilter
