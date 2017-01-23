# -*- coding: utf-8 -*-

# Librerias django

# Django Atajos
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

# Django Login
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Django Messages
from django.contrib import messages

# Django Generic Views
from django.views.generic.base import View
from django.views.generic import ListView

# Django Autorizacion
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Formularios:
from .forms import UsuarioCreateForm
from .forms import UsuarioEditForm
from .forms import ProfileForm

# API Rest:
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

# API Rest - Serializadores:
from .serializers import UserSerializer


class Login(View):

    def __init__(self):
        self.template_name = 'login.html'

    def get(self, request):

        if request.user.is_authenticated():
            return redirect(reverse('dashboards:inicio'))

        else:
            return render(request, self.template_name, {})

    def post(self, request):

        usuario = request.POST.get('username')
        contrasena = request.POST.get('password')

        user = authenticate(username=usuario, password=contrasena)

        if user is not None:

            if user.is_active:
                login(request, user)
                return redirect(reverse('dashboards:inicio'))
            else:
                messages.warning(
                    request,
                    "Cuenta DESACTIVADA, favor de contactara a su administrador"
                )

        else:
            messages.error(request, "Cuenta usuario o contraseña no valida")

        return render(request, self.template_name, {})


@method_decorator(login_required, name='dispatch')
class UsuarioListView(ListView):

    template_name = 'usuario/lista.html'
    model = User
    context_object_name = 'usuarios'
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class UsuarioCreateView(View):

    def __init__(self):
        self.template_name = 'usuario/crear.html'

    def obtener_UrlImagen(self, _imagen):
        imagen = ''

        if _imagen:
            imagen = _imagen.url

        return imagen

    def get(self, request):
        formulario = UsuarioCreateForm()
        formulario_profile = ProfileForm()

        contexto = {
            'form': formulario,
            'form_profile': formulario_profile,
            'operation': "Nuevo"
        }
        return render(request, self.template_name, contexto)

    def post(self, request):

        formulario = UsuarioCreateForm(request.POST)
        formulario_profile = ProfileForm(
            request.POST,
            request.FILES
        )

        if formulario.is_valid() and formulario_profile.is_valid():

            datos_formulario = formulario.cleaned_data

            usuario = User.objects.create_user(
                username=datos_formulario.get('username'),
                password=datos_formulario.get('password')
            )
            usuario.first_name = datos_formulario.get('first_name')
            usuario.last_name = datos_formulario.get('last_name')
            usuario.email = datos_formulario.get('email')
            usuario.is_active = datos_formulario.get('is_active')

            usuario.is_staff = datos_formulario.get('is_staff')

            if datos_formulario.get('is_staff'):
                usuario.is_superuser = True
            else:
                usuario.is_superuser = False

            usuario.save()

            datos_profile = formulario_profile.cleaned_data

            usuario.profile.puesto = datos_profile.get('puesto')
            usuario.profile.clave = datos_profile.get('clave')
            usuario.profile.fecha_nacimiento = datos_profile.get(
                'fecha_nacimiento'
            )
            usuario.profile.imagen = datos_profile.get('imagen')
            usuario.profile.save()

            return redirect(
                reverse('seguridad:usuarios_lista')
            )

        else:
            contexto = {
                'form': formulario,
                'form_profile': formulario_profile,
                'operation': "Nuevo"
            }
            return render(request, self.template_name, contexto)


@method_decorator(login_required, name='dispatch')
class UsuarioEditView(View):

    def __init__(self):
        self.template_name = 'usuario/modificar.html'
        self.cuenta = ''

    def obtener_UrlImagen(self, _imagen):
        imagen = ''

        if _imagen:
            imagen = _imagen.url

        return imagen

    def get(self, request, pk):

        usuario = get_object_or_404(User, pk=pk)
        self.cuenta = usuario.username

        formulario = UsuarioEditForm(
            initial={
                'username': usuario.username,
                'first_name': usuario.first_name,
                'last_name': usuario.last_name,
                'email': usuario.email,
                'is_staff': usuario.is_staff,
                'is_active': usuario.is_active,
            }
        )

        formulario_profile = ProfileForm(
            initial={
                'puesto': usuario.profile.puesto,
                'clave': usuario.profile.clave,
                'fecha_nacimiento': usuario.profile.fecha_nacimiento,
                'imagen': usuario.profile.imagen,
                'comentarios': usuario.profile.comentarios,
            }
        )

        contexto = {
            'form': formulario,
            'form_profile': formulario_profile,
            'cuenta': self.cuenta,
            'imagen': self.obtener_UrlImagen(usuario.profile.imagen),
            'operation': "Editar"
        }
        return render(request, self.template_name, contexto)

    def post(self, request, pk):

        formulario = UsuarioEditForm(request.POST)

        usuario = get_object_or_404(User, pk=pk)
        self.cuenta = usuario.username

        formulario_profile = ProfileForm(
            request.POST,
            request.FILES,
        )

        if formulario.is_valid() and formulario_profile.is_valid():

            datos_formulario = formulario.cleaned_data
            usuario.first_name = datos_formulario.get('first_name')
            usuario.last_name = datos_formulario.get('last_name')
            usuario.email = datos_formulario.get('email')
            usuario.is_staff = datos_formulario.get('is_staff')
            usuario.is_active = datos_formulario.get('is_active')

            if datos_formulario.get('is_staff'):
                usuario.is_superuser = True
            else:
                usuario.is_superuser = False

            if datos_formulario.get('password'):
                usuario.password = make_password(
                    datos_formulario.get('password'))

            usuario.save()

            datos_profile = formulario_profile.cleaned_data

            usuario.profile.puesto = datos_profile.get('puesto')
            usuario.profile.clave = datos_profile.get('clave')
            usuario.profile.fecha_nacimiento = datos_profile.get(
                'fecha_nacimiento'
            )
            usuario.profile.imagen = datos_profile.get('imagen')
            usuario.profile.save()

            return redirect(
                reverse('seguridad:usuarios_lista')
            )

        contexto = {
            'form': formulario,
            'form_profile': formulario_profile,
            'imagen': self.obtener_UrlImagen(usuario.profile.imagen),
            'cuenta': self.cuenta,
            'operation': "Editar"
        }
        return render(request, self.template_name, contexto)


class UserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('username', 'is_active')
