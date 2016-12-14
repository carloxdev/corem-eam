# -*- coding: utf-8 -*-

# LIBRERIAS Django

# Django Atajos:
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

# Django Urls:
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

# Django Paginator
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# Django Generic Views
from django.views.generic.base import View
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import TemplateView

# Modelos:
from .models import Equipo
from .models import Ubicacion
from home.models import AnexoImagen
from home.models import AnexoArchivo
from home.models import AnexoTexto

# Formularios:
from forms import EquipoFiltersForm
from forms import EquipoForm
from forms import UbicacionForm
from home.forms import AnexoTextoForm
from home.forms import AnexoImagenForm
from home.forms import AnexoArchivoForm

# API Rest:
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# API Rest - Serializadores:
from .serializers import EquipoSerializer
from .serializers import EquipoTreeSerilizado
from .serializers import UbicacionSerializer
from home.serializers import AnexoTextoSerializer
from home.serializers import AnexoArchivoSerializer
from home.serializers import AnexoImagenSerializer

# API Rest - Paginacion:
from .pagination import GenericPagination

# API Rest - Filtros:
from .filters import EquipoFilter


# ----------------- EQUIPO ----------------- #

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


class EquipoCreateView(View):

    def __init__(self):
        self.template_name = 'equipo/formulario.html'

    def get(self, request):
        formulario = EquipoForm()
        contexto = {
            'form': formulario,
        }

        return render(request, self.template_name, contexto)

    def post(self, request):

        formulario = EquipoForm(request.POST)

        if formulario.is_valid():

            datos_formulario = formulario.cleaned_data
            equipo = Equipo()
            equipo.tag = datos_formulario.get('tag')
            equipo.descripcion = datos_formulario.get('descripcion')
            equipo.serie = datos_formulario.get('serie')
            equipo.tipo = datos_formulario.get('tipo')
            equipo.estado = datos_formulario.get('estado')
            equipo.padre = datos_formulario.get('padre')
            equipo.empresa = datos_formulario.get('empresa')
            equipo.sistema = datos_formulario.get('sistema')
            equipo.ubicacion = datos_formulario.get('ubicacion')
            if 'imagen' in request.POST:
                equipo.imagen = request.POST['imagen']
            else:
                equipo.imagen = request.FILES['imagen']
            equipo.save()

            return redirect(
                reverse('activos.equipos_lista')
            )

        contexto = {
            'form': formulario
        }
        return render(request, self.template_name, contexto)


class EquipoUpdateView(View):
    def __init__(self):
        self.template_name = 'equipo/formulario.html'
        self.tag = ''

    def get(self, request, pk):

        equipo = get_object_or_404(Equipo, pk=pk)
        self.tag = equipo.tag

        formulario = EquipoForm(
            initial={
                'descripcion': equipo.descripcion,
                'serie': equipo.serie,
                'tipo': equipo.tipo,
                'estado': equipo.estado,
                'padre': equipo.padre,
                'empresa': equipo.empresa,
                'sistema': equipo.sistema,
                'ubicacion': equipo.ubicacion,
            }
        )

        contexto = {
            'form': formulario,
            'tag': self.tag
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):

        formulario = EquipoForm(request.POST)

        equipo = get_object_or_404(Equipo, pk=pk)
        self.tag = equipo.tag

        if formulario.is_valid():

            datos_formulario = formulario.cleaned_data
            equipo.descripcion = datos_formulario.get('descripcion')
            equipo.serie = datos_formulario.get('serie')
            equipo.tipo = datos_formulario.get('tipo')
            equipo.estado = datos_formulario.get('estado')
            equipo.padre = datos_formulario.get('padre')
            equipo.empresa = datos_formulario.get('empresa')
            equipo.sistema = datos_formulario.get('sistema')
            equipo.ubicacion = datos_formulario.get('ubicacion')

            equipo.save()

            return redirect(
                reverse('activos.equipos_lista')
            )

        contexto = {
            'form': formulario,
            'tag': self.tag
        }
        return render(request, self.template_name, contexto)


class EquipoAPI(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    pagination_class = GenericPagination

    filter_backends = (DjangoFilterBackend,)
    filter_class = EquipoFilter


class EquipoTreeListView(View):

    def __init__(self):
        self.template_name = "equipo/arbol.html"

    def get(self, request, pk):

        equipo = get_object_or_404(Equipo, pk=pk)

        contexto = {
            "equipo": equipo
        }

        return render(request, self.template_name, contexto)


class EquipoTreeAPI(View):

    def get(self, request, pk):

        daddies = Equipo.objects.filter(pk=pk)

        serializador = EquipoTreeSerilizado()
        lista_json = serializador.get_Json(daddies)

        return HttpResponse(
            lista_json,
            content_type="application/json"
        )


# ----------------- EQUIPO - ANEXO ----------------- #

class AnexoTextoView(View):

    def __init__(self):
        self.template_name = 'equipo/anexos_texto.html'

    def get(self, request, pk):
        id_equipo = pk
        texto = AnexoTexto.objects.filter(equipo=id_equipo)
        paginator = Paginator(texto, 5)
        pagina = request.GET.get('page')
        try:
            anexos = paginator.page(pagina)
        except PageNotAnInteger:
            anexos = paginator.page(1)
        except EmptyPage:
            anexos = paginator.page(paginator.num_pages)
        form = AnexoTextoForm()

        contexto = {
            'form': form,
            'id': id_equipo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):
        id_equipo = pk
        form = AnexoTextoForm(request.POST)
        if form.is_valid():
            texto = form.save(commit=False)
            texto.equipo_id = id_equipo
            texto.save()

        return redirect(reverse_lazy('activos.equipos_lista'))


class AnexoImagenView(View):

    def __init__(self):
        self.template_name = 'equipo/anexos_imagen.html'

    def get(self, request, pk):
        id_equipo = pk
        imagen = AnexoImagen.objects.filter(equipo=id_equipo)
        paginator = Paginator(imagen, 5)
        pagina = request.GET.get('page')
        try:
            anexos = paginator.page(pagina)
        except PageNotAnInteger:
            anexos = paginator.page(1)
        except EmptyPage:
            anexos = paginator.page(paginator.num_pages)
        form = AnexoImagenForm()

        contexto = {
            'form': form,
            'id': id_equipo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):
        id_equipo = pk
        form = AnexoImagenForm(request.POST)
        if form.is_valid():
            imagenAnexo = AnexoImagen()
            imagenAnexo.descripcion = request.POST['descripcion']
            if 'ruta' in request.POST:
                imagenAnexo.ruta = request.POST['ruta']
            else:
                imagenAnexo.ruta = request.FILES['ruta']
                imagenAnexo.equipo_id = id_equipo
                imagenAnexo.save()
            imagenAnexo.equipo_id = id_equipo
            imagenAnexo.save()

        return render(request, 'equipo/anexos_texto.html', {'form': form, 'id': id_equipo})


class AnexoArchivoView(View):

    def __init__(self):
        self.template_name = 'equipo/anexos_archivo.html'

    def get(self, request, pk):
        id_equipo = pk
        archivo = AnexoArchivo.objects.filter(equipo=id_equipo)
        paginator = Paginator(archivo, 5)
        pagina = request.GET.get('page')
        try:
            anexos = paginator.page(pagina)
        except PageNotAnInteger:
            anexos = paginator.page(1)
        except EmptyPage:
            anexos = paginator.page(paginator.num_pages)
        form = AnexoArchivoForm()

        contexto = {
            'form': form,
            'id': id_equipo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):
        id_equipo = pk
        form = AnexoArchivoForm(request.POST)

        if form.is_valid():
            archivo = AnexoArchivo()
            archivo.descripcion = request.POST['descripcion']
            if 'archivo' in request.POST:
                archivo.archivo = request.POST['archivo']
            else:
                archivo.archivo = request.FILES['archivo']
                archivo.equipo_id = id_equipo
                archivo.save()
            archivo.equipo_id = id_equipo
            archivo.save()
        return render(request, 'equipo/anexos_archivo.html', {'form': form, 'id': id_equipo})


class AnexoTextoAPI(viewsets.ModelViewSet):
    queryset = AnexoTexto.objects.all()
    serializer_class = AnexoTextoSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('equipo',)


class AnexoArchivoAPI(viewsets.ModelViewSet):
    queryset = AnexoArchivo.objects.all()
    serializer_class = AnexoArchivoSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('equipo',)


class AnexoImagenAPI(viewsets.ModelViewSet):
    queryset = AnexoImagen.objects.all()
    serializer_class = AnexoImagenSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('equipo',)


# ----------------- UBICACION ----------------- #

class UbicacionListView(TemplateView):
    template_name = 'ubicacion/lista.html'


class UbicacionCreateView(CreateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'ubicacion/formulario.html'
    success_url = reverse_lazy('activos.ubicaciones_lista')


class UbicacionUpdateView(UpdateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'ubicacion/formulario.html'
    success_url = reverse_lazy('activos.ubicaciones_lista')


class UbicacionAPI(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('clave', 'descripcion',)
