# -*- coding: utf-8 -*-

# LIBRERIAS Django

# Django DB
from django.db import transaction

# Django Atajos:
from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

# Django Urls:
from django.core.urlresolvers import reverse
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
from .models import UdmArticulo
from .models import Almacen
from .models import Stock
from .models import EntradaCabecera
from .models import EntradaDetalle
from .models import SalidaCabecera
from .models import SalidaDetalle
from home.models import AnexoImagen
from home.models import AnexoArchivo
from home.models import AnexoTexto


# Formularios:
from .forms import AlmacenForm
from .forms import ArticuloFilterForm
from .forms import ArticuloForm
from .forms import EntradaCabeceraFilterForm
from .forms import EntradaCabeceraForm
from .forms import StockFilterForm
from .forms import EntradaDetalleForm
from .forms import UdmArticuloForm

from home.forms import AnexoTextoForm
from home.forms import AnexoImagenForm
from home.forms import AnexoArchivoForm

# API Rest:
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# API Rest - Serializadores:
from .serializers import AlmacenSerializer
from .serializers import UdmArticuloSerializer
from .serializers import ArticuloSerializer
from .serializers import StockSerializer
from .serializers import EntradaCabeceraSerializer
from .serializers import EntradaDetalleSerializer
from .serializers import SalidaCabeceraSerializer
from home.serializers import AnexoTextoSerializer
from home.serializers import AnexoImagenSerializer
from home.serializers import AnexoArchivoSerializer

# API Rest - Paginacion:
from .pagination import GenericPagination

# API Rest - Filtros:
from .filters import ArticuloFilter
from .filters import EntradaCabeceraFilter
from .filters import StockFilter

# ----------------- ALMACEN ----------------- #


class AlmacenListView(TemplateView):
    template_name = 'almacen/lista.html'


class AlmacenCreateView(CreateView):
    model = Almacen
    form_class = AlmacenForm
    template_name = 'almacen/formulario.html'
    success_url = reverse_lazy('inventarios:almacenes_lista')

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


# ----------------- UDM ARTICULO ----------------- #

class UdmArticuloListView(TemplateView):
    template_name = 'udm_articulo/lista.html'


class UdmArticuloCreateView(CreateView):
    model = UdmArticulo
    form_class = UdmArticuloForm
    template_name = 'udm_articulo/formulario.html'
    success_url = reverse_lazy('inventarios:udms_articulo_lista')
    operation = "Nueva"

    def get_context_data(self, **kwargs):
        contexto = super(
            UdmArticuloCreateView,
            self
        ).get_context_data(**kwargs)
        contexto['operation'] = self.operation
        return contexto


class UdmArticuloUpdateView(UpdateView):
    model = UdmArticulo
    form_class = UdmArticuloForm
    template_name = 'udm_articulo/formulario.html'
    success_url = reverse_lazy('inventarios:udms_articulo_lista')
    operation = "Editar"

    def get_context_data(self, **kwargs):
        contexto = super(
            UdmArticuloUpdateView,
            self
        ).get_context_data(**kwargs)
        contexto['operation'] = self.operation
        return contexto


class UdmArticuloAPI(viewsets.ModelViewSet):
    queryset = UdmArticulo.objects.all()
    serializer_class = UdmArticuloSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('clave', 'descripcion',)


class UdmArticuloAPI2(viewsets.ModelViewSet):
    queryset = UdmArticulo.objects.all()
    serializer_class = UdmArticuloSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)


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


class ArticuloCreateView(View):
    def __init__(self):
        self.template_name = 'articulo/formulario.html'

    def get(self, request):
        formulario = ArticuloForm()
        contexto = {
            'form': formulario,
            'operation': "Nuevo"
        }
        return render(request, self.template_name, contexto)

    def post(self, request):

        formulario = ArticuloForm(request.POST)

        if formulario.is_valid():
            datos_formulario = formulario.cleaned_data
            articulo = Articulo()
            articulo.clave = datos_formulario.get('clave')
            articulo.descripcion = datos_formulario.get('descripcion')
            articulo.tipo = datos_formulario.get('tipo')
            articulo.udm = datos_formulario.get('udm')
            articulo.estado = datos_formulario.get('estado')
            articulo.clave_jde = datos_formulario.get('clave_jde')
            articulo.save()

            return redirect(
                reverse('inventarios:articulos_lista')
            )
        contexto = {
            'form': formulario,
            'operation': "Nuevo"
        }

        return render(request, self.template_name, contexto)


class ArticuloUpdateView(UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo/formulario.html'
    success_url = reverse_lazy('inventarios:articulos_lista')

    def get_context_data(self, **kwargs):
        context = super(ArticuloUpdateView, self).get_context_data(**kwargs)

        data = {
            'operation': "Editar"
        }

        context.update(data)

        return context


class ArticuloAPI(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    pagination_class = GenericPagination

    filter_backends = (DjangoFilterBackend,)
    filter_class = ArticuloFilter


class ArticuloFormAPI(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ArticuloFilter


# ----------------- ARTICULO - ANEXOS ----------------- #

class ArticuloAnexoTextoView(View):

    def __init__(self):
        self.template_name = 'articulo/anexos/anexos_texto.html'

    def get(self, request, pk):
        id_articulo = pk
        anexos = AnexoTexto.objects.filter(articulo=id_articulo)
        articulo = Articulo.objects.get(id=id_articulo)
        form = AnexoTextoForm()

        contexto = {
            'form': form,
            'id': id_articulo,
            'articulo': articulo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):
        id_articulo = pk
        form = AnexoTextoForm(request.POST)
        anexos = AnexoTexto.objects.filter(articulo=id_articulo)
        articulo = Articulo.objects.get(id=id_articulo)

        if form.is_valid():
            texto = form.save(commit=False)
            texto.articulo_id = id_articulo
            texto.save()
            anexos = AnexoTexto.objects.filter(articulo=id_articulo)
            form = AnexoTextoForm()
        return render(request, 'articulo/anexos/anexos_texto.html',
                      {'form': form, 'id': id_articulo, 'anexos': anexos,
                       'articulo': articulo})


class ArticuloAnexoImagenView(View):

    def __init__(self):
        self.template_name = 'articulo/anexos/anexos_imagen.html'

    def get(self, request, pk):
        id_articulo = pk
        anexos = AnexoImagen.objects.filter(articulo=id_articulo)
        articulo = Articulo.objects.get(id=id_articulo)
        form = AnexoImagenForm()

        contexto = {
            'form': form,
            'id': id_articulo,
            'articulo': articulo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):
        id_articulo = pk
        anexos = AnexoImagen.objects.filter(articulo=id_articulo)
        articulo = Articulo.objects.get(id=id_articulo)
        form = AnexoImagenForm(request.POST, request.FILES)

        if form.is_valid():
            imagen_anexo = AnexoImagen()
            imagen_anexo.descripcion = request.POST['descripcion']
            if 'ruta' in request.POST:
                imagen_anexo.ruta = request.POST['ruta']
            else:
                imagen_anexo.ruta = request.FILES['ruta']
            imagen_anexo.articulo_id = id_articulo
            imagen_anexo.save()
            form = AnexoImagenForm()
            anexos = AnexoImagen.objects.filter(articulo=id_articulo)

        contexto = {
            'form': form,
            'id': id_articulo,
            'articulo': articulo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)


class ArticuloAnexoArchivoView(View):

    def __init__(self):
        self.template_name = 'articulo/anexos/anexos_archivo.html'

    def get(self, request, pk):
        id_articulo = pk
        anexos = AnexoArchivo.objects.filter(articulo=id_articulo)
        articulo = Articulo.objects.get(id=id_articulo)
        form = AnexoArchivoForm()

        contexto = {
            'form': form,
            'id': id_articulo,
            'articulo': articulo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):
        id_articulo = pk
        articulo = Articulo.objects.get(id=id_articulo)
        anexos = AnexoArchivo.objects.filter(articulo=id_articulo)
        form = AnexoArchivoForm(request.POST, request.FILES)

        if form.is_valid():
            archivo_anexo = AnexoArchivo()
            archivo_anexo.descripcion = request.POST['descripcion']
            if 'archivo' in request.POST:
                archivo_anexo.archivo = request.POST['archivo']
            else:
                archivo_anexo.archivo = request.FILES['archivo']
            archivo_anexo.articulo_id = id_articulo
            archivo_anexo.save()
            anexos = AnexoArchivo.objects.filter(articulo=id_articulo)
            form = AnexoArchivoForm()

            contexto = {
                'form': form,
                'id': id_articulo,
                'articulo': articulo,
                'anexos': anexos,
            }

            return render(request, self.template_name, contexto)


class ArticuloAnexoTextoAPI(viewsets.ModelViewSet):
    queryset = AnexoTexto.objects.all()
    serializer_class = AnexoTextoSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('articulo',)


class ArticuloAnexoImagenAPI(viewsets.ModelViewSet):
    queryset = AnexoImagen.objects.all()
    serializer_class = AnexoImagenSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('articulo',)


class ArticuloAnexoArchivoAPI(viewsets.ModelViewSet):
    queryset = AnexoArchivo.objects.all()
    serializer_class = AnexoArchivoSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('articulo',)


# ----------------- STOCK ----------------- #

class StockListView(View):
    template_name = 'stock/lista.html'

    def get(self, request, pk):

        formulario = StockFilterForm()

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):
        return render(request, self.template_name, {})


class StockAPI(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    pagination_class = GenericPagination

    filter_backends = (DjangoFilterBackend,)
    filter_class = StockFilter

# -----------------  ENTRADAS  ----------------- #


class EntradaCabeceraListView(View):
    def __init__(self):
        self.template_name = 'entrada/lista.html'

    def get(self, request):

        formulario = EntradaCabeceraFilterForm()

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)


class EntradaCabeceraCreateView(View):
    def __init__(self):
        self.template_name = 'entrada/formulario.html'

    def get(self, request):

        formulario = EntradaCabeceraForm()
        contexto = {
            'form': formulario,
        }

        return render(request, self.template_name, contexto)

    def post(self, request):

        formulario = EntradaCabeceraForm(request.POST)
        detalle_form = EntradaDetalleForm(request.POST)
        id_ent_cabecera = request.POST.get('cabecera')
        if formulario.is_valid():
            datos_formulario = formulario.cleaned_data
            entrada_cabecera = EntradaCabecera()
            entrada_cabecera.clave = datos_formulario.get('clave')
            entrada_cabecera.descripcion = datos_formulario.get('descripcion')
            entrada_cabecera.fecha = datos_formulario.get('fecha')
            entrada_cabecera.almacen = datos_formulario.get('almacen')
            entrada_cabecera.save()

            id_cabecera = entrada_cabecera.id
            print id_cabecera
            formulario_detalle = EntradaDetalleForm()
            contexto = {
                'form': formulario,
                'id_cabecera': id_cabecera,
                'form_detalle': formulario_detalle,
            }
            return render(request, self.template_name, contexto)

        if detalle_form.is_valid():
            id_cabecera = request.POST.get('cabecera')
            obj_cabecera = EntradaCabecera.objects.get(id=id_cabecera)
            datos_formulario = detalle_form.cleaned_data
            entrada_detalle = EntradaDetalle()
            entrada_detalle.articulo = datos_formulario.get('articulo')
            entrada_detalle.cantidad = datos_formulario.get('cantidad')
            entrada_detalle.cabecera = obj_cabecera
            entrada_detalle.save()

            detalles = EntradaDetalle.objects.filter(cabecera=id_ent_cabecera)
            formulario_detalle = EntradaDetalleForm()

            contexto = {
                'form': formulario,
                'id_cabecera': id_cabecera,
                'form_detalle': formulario_detalle,
                'detalles': detalles,
            }

            return render(request, self.template_name, contexto)

        contexto = {
            'form': formulario,
        }
        return render(request, self.template_name, contexto)


class EntradaAPI(viewsets.ModelViewSet):
    queryset = EntradaCabecera.objects.all()
    serializer_class = EntradaCabeceraSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = EntradaCabeceraFilter


class EntradaDetalleAPI(viewsets.ModelViewSet):
    queryset = EntradaDetalle.objects.all()
    serializer_class = EntradaDetalleSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('cabecera',)


# -----------------  SALIDAS  ----------------- #
