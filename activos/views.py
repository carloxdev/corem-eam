# -*- coding: utf-8 -*-

# Django Atajos:
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

# Django Urls:
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

# Django Generic Views
from django.views.generic.base import View
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import TemplateView

# Modelos:
from .models import Equipo
from .models import Odometro
from .models import Ubicacion
from .models import Medicion
from home.models import AnexoImagen
from home.models import AnexoArchivo
from home.models import AnexoTexto

# Formularios:
from forms import EquipoFiltersForm
from forms import EquipoForm
from forms import UbicacionForm
from forms import OdometroForm
from forms import OdometroFiltersForm
from forms import MedicionFiltersForm
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
from .serializers import OdometroSerializer
from .serializers import MedicionSerializer
from home.serializers import AnexoTextoSerializer
from home.serializers import AnexoArchivoSerializer
from home.serializers import AnexoImagenSerializer

# API Rest - Paginacion:
from .pagination import GenericPagination

# API Rest - Filtros:
from .filters import EquipoFilter
from .filters import OdometroFilter


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

        formulario = EquipoForm(request.POST, request.FILES)

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
                'tag': equipo.tag,
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
            equipo.tag = datos_formulario.get('tag')
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
        self.template_name = 'equipo/anexos/anexos_texto.html'

    def get(self, request, pk):
        id_equipo = pk
        anexos = AnexoTexto.objects.filter(equipo=id_equipo)
        equipo = Equipo.objects.get(id=id_equipo)
        form = AnexoTextoForm()

        contexto = {
            'form': form,
            'id': id_equipo,
            'equipo': equipo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):
        id_equipo = pk
        form = AnexoTextoForm(request.POST)
        anexos = AnexoTexto.objects.filter(equipo=id_equipo)
        equipo = Equipo.objects.get(id=id_equipo)

        if form.is_valid():
            texto = form.save(commit=False)
            texto.equipo_id = id_equipo
            texto.save()
            anexos = AnexoTexto.objects.filter(equipo=id_equipo)
            form = AnexoTextoForm()
        return render(request, 'equipo/anexos/anexos_texto.html',
                      {'form': form, 'id': id_equipo, 'anexos': anexos,
                       'equipo': equipo})


class AnexoImagenView(View):

    def __init__(self):
        self.template_name = 'equipo/anexos/anexos_imagen.html'

    def get(self, request, pk):
        id_equipo = pk
        anexos = AnexoImagen.objects.filter(equipo=id_equipo)
        equipo = Equipo.objects.get(id=id_equipo)
        form = AnexoImagenForm()

        contexto = {
            'form': form,
            'id': id_equipo,
            'equipo': equipo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):
        id_equipo = pk
        anexos = AnexoImagen.objects.filter(equipo=id_equipo)
        equipo = Equipo.objects.get(id=id_equipo)
        form = AnexoImagenForm(request.POST, request.FILES)

        if form.is_valid():

            imagen_anexo = AnexoImagen()
            imagen_anexo.descripcion = request.POST['descripcion']
            if 'ruta' in request.POST:
                imagen_anexo.ruta = request.POST['ruta']
            else:
                imagen_anexo.ruta = request.FILES['ruta']
            imagen_anexo.equipo_id = id_equipo
            imagen_anexo.save()
            form = AnexoImagenForm()
            anexos = AnexoImagen.objects.filter(equipo=id_equipo)
            # return render(request, self.template_name,
            #               {'form': form, 'id': id_equipo, 'anexos': anexos,
            #                'equipo': equipo})
        contexto = {
            'form': form,
            'id': id_equipo,
            'equipo': equipo,
            'anexos': anexos,
        }
        return render(request, self.template_name, contexto)


class AnexoArchivoView(View):

    def __init__(self):
        self.template_name = 'equipo/anexos/anexos_archivo.html'

    def get(self, request, pk):
        id_equipo = pk
        anexos = AnexoArchivo.objects.filter(equipo=id_equipo)
        equipo = Equipo.objects.get(id=id_equipo)
        form = AnexoArchivoForm()

        contexto = {
            'form': form,
            'id': id_equipo,
            'equipo': equipo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):
        id_equipo = pk
        equipo = Equipo.objects.get(id=id_equipo)
        form = AnexoArchivoForm(request.POST, request.FILES)
        anexos = AnexoArchivo.objects.filter(equipo=id_equipo)

        if form.is_valid():
            archivo_anexo = AnexoArchivo()
            archivo_anexo.descripcion = request.POST['descripcion']
            if 'archivo' in request.POST:
                archivo_anexo.archivo = request.POST['archivo']
            else:
                archivo_anexo.archivo = request.FILES['archivo']
            archivo_anexo.equipo_id = id_equipo
            archivo_anexo.save()
            anexos = AnexoArchivo.objects.filter(equipo=id_equipo)
            form = AnexoArchivoForm()

        contexto = {
            'form': form,
            'id': id_equipo,
            'equipo': equipo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)


class AnexoTextoAPI(viewsets.ModelViewSet):
    queryset = AnexoTexto.objects.all()
    serializer_class = AnexoTextoSerializer
    pagination_class = GenericPagination


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

# ----------------- ODOMETRO ----------------- #


class OdometroListView(View):
    def __init__(self):
        self.template_name = 'odometro/lista.html'

    def get(self, request):

        formulario = OdometroFiltersForm()

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)

    def post(self, request):
        return render(request, self.template_name, {})


class OdometroCreateView(CreateView):
    model = Odometro
    form_class = OdometroForm
    template_name = 'odometro/formulario.html'
    success_url = reverse_lazy('activos.odometros_lista')


class OdometroUpdateView(UpdateView):
    model = Odometro
    form_class = OdometroForm
    template_name = 'odometro/formulario.html'
    success_url = reverse_lazy('activos.odometros_lista')


class OdometroAPI(viewsets.ModelViewSet):
    queryset = Odometro.objects.all()
    serializer_class = OdometroSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = OdometroFilter

# ----------------- MEDICION ----------------- #


class MedicionListView(View):

    def __init__(self):
        self.template_name = 'medicion/lista.html'

    def get(self, request):

        formulario = MedicionFiltersForm()

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)


class MedicionCreateView(View):
    pass


class MedicionAPI(viewsets.ModelViewSet):
    queryset = Medicion.objects.all().order_by('-fecha')
    serializer_class = MedicionSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('odometro',)
