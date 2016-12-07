# -*- coding: utf-8 -*-
# Librerias Python
import json
# Librerias django

# Django Atajos
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

# Django Urls:
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse

# Django Generic Views
from django.views.generic.base import View
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import TemplateView

# Modelos:
from .models import Equipo, Ubicacion

# API Rest:
from rest_framework import viewsets

# API Rest - Serializadores:
from .serializers import EquipoSerializer, UbicacionSerializer
# API Rest - Paginacion:
from .pagination import GenericPagination

# Formularios:
from forms import EquipoFiltersForm
from forms import EquipoCreateForm
from forms import EquipoUpdateForm
from forms import UbicacionFiltersForm
from forms import UbicacionCreateForm
from forms import TextoForm


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
        self.template_name = 'equipo/nuevo.html'

    def get(self, request):
        ins = Equipo()
        hijos = ins.get_all_children()
        print hijos
        formulario = EquipoCreateForm()
        contexto = {
            'form': formulario,
        }

        return render(request, self.template_name, contexto)

    def post(self, request):

        formulario = EquipoCreateForm(request.POST)

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
        self.template_name = 'equipo/editar.html'
        self.tag = ''

    def get(self, request, pk):

        equipo = get_object_or_404(Equipo, pk=pk)
        self.tag = equipo.tag

        formulario = EquipoUpdateForm(
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

        formulario = EquipoUpdateForm(request.POST)

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


class UbicacionAPI(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
    pagination_class = GenericPagination


class EquipoTreeListView(TemplateView):
    template_name = "equipo/arbol.html"


def obtener_arbol(request):
    tree = {'text': '', 'nodes': []}
    sub_tree = tree['nodes']

    def print_Hijos(_hijos, _tag):

        _tag += "--"

        for hijo in _hijos:
            print "{} Hijo: {}".format(_tag, hijo)
            hijos = Equipo.objects.filter(padre=hijo)
            if len(hijos) > 0:
                print_Hijos(hijos, _tag)

        return None

    daddies = Equipo.objects.filter(padre=None)
    tag = "--"

    for daddy in daddies:

        print "Padre: {}".format(daddy)

        hijos = Equipo.objects.filter(padre=daddy)
        print_Hijos(hijos, tag)

    return HttpResponse(json.dumps(tree), content_type="application/json")

# ----------------- UBICACION ----------------- #


class UbicacionCreateView(CreateView):
    model = Ubicacion
    form_class = UbicacionCreateForm
    template_name = 'ubicacion/formulario.html'
    success_url = reverse_lazy('activos.ubicaciones_lista')


class UbicacionListView(View):

    def __init__(self):
        self.template_name = 'ubicacion/lista.html'

    def get(self, request):

        formulario = UbicacionFiltersForm()

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)

    def post(self, request):
        return render(request, self.template_name, {})


class UbicacionUpdateView(UpdateView):
    model = Ubicacion
    form_class = UbicacionCreateForm
    template_name = 'ubicacion/formulario.html'
    success_url = reverse_lazy('activos.ubicaciones_lista')


def anexos(request, **kwargs):
    e_id = kwargs.get('pk', 0)
    equipo = Equipo.objects.get(id=e_id)
    contexto = {'id': e_id}
    print equipo
    return render(request, 'equipo/anexos.html', contexto)


def anexar_texto(request, **kwargs):
    id_e = kwargs.get('pk', 0)
    equipo = Equipo.objects.get(id=id_e)
    equipo_id = equipo.id
    # print equipo
    if request.method == 'GET':
        form = TextoForm()
        id = id_e
    else:
        form = TextoForm(request.POST)
        if form.is_valid():
            texto = form.save()
            texto.equipo = equipo_id
            texto.save()
        return redirect('equipos/')
    return render(request, 'equipo/anexos_texto.html', {'form':form, 'id': id_e})
