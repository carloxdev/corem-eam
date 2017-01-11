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

# Django Generic Views
from django.views.generic.base import View
from django.views.generic import ListView

# Django Autorizacion
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Formularios:
from .forms import UsuarioCreateForm
from .forms import UsuarioEditForm


# class Login(View):

#     def __init__(self):
#         self.template_name = 'login.html'

#     def get(self, request):

#         if request.user.is_authenticated():
#             return redirect(reverse('home.dashboard'))

#         else:
#             return render(request, self.template_name, {})

#     def post(self, request):

#         mensaje = ''
#         usuario = request.POST.get('user')
#         contrasena = request.POST.get('password')

#         user = authenticate(username=usuario, password=contrasena)

#         if user is not None:

#             if user.is_active:
#                 login(request, user)
#                 return redirect(reverse('home.dashboard'))
#             else:
#                 mensaje = "Cuenta desactivada"

#         else:
#             mensaje = "Cuenta usuario o contraseña no vaida"

#         contexto = {
#             'mensaje': mensaje
#         }

#         return render(request, self.template_name, contexto)


class Dashboard(View):

    def __init__(self):
        self.template_name = 'dashboard.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        return render(request, self.template_name, {})


class Login(View):

    def __init__(self):
        self.template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        return redirect(reverse('seguridad.dashboard'))
        # return render(request, self.template_name, {})


# @method_decorator(login_required, name='dispatch')
class UsuarioListView(ListView):

    template_name = 'usuario/lista.html'
    model = User
    context_object_name = 'usuarios'
    paginate_by = 10


# @method_decorator(login_required, name='dispatch')
class UsuarioCreateView(View):

    def __init__(self):
        self.template_name = 'usuario/crear.html'

    def get(self, request):
        formulario = UsuarioCreateForm()
        contexto = {
            'form': formulario,
            'operation': "Nuevo"
        }
        return render(request, self.template_name, contexto)

    def post(self, request):

        formulario = UsuarioCreateForm(request.POST)

        if formulario.is_valid():

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

            return redirect(
                reverse('seguridad.usuarios_lista')
            )

        else:
            contexto = {
                'form': formulario,
                'operation': "Nuevo"
            }
            return render(request, self.template_name, contexto)


# @method_decorator(login_required, name='dispatch')
class UsuarioEditView(View):

    def __init__(self):
        self.template_name = 'usuario/modificar.html'
        self.cuenta = ''

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

        contexto = {
            'form': formulario,
            'cuenta': self.cuenta,
            'operation': "Editar"
        }
        return render(request, self.template_name, contexto)

    def post(self, request, pk):

        formulario = UsuarioEditForm(request.POST)

        usuario = get_object_or_404(User, pk=pk)
        self.cuenta = usuario.username

        if formulario.is_valid():
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

            return redirect(
                reverse('seguridad.usuarios_lista')
            )

        contexto = {
            'form': formulario,
            'cuenta': self.cuenta,
            'operation': "Editar"
        }
        return render(request, self.template_name, contexto)
