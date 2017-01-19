# -*- coding: utf-8 -*-

# Librerias Django
from django.forms import ModelForm
from django.forms import EmailInput
from django.forms import TextInput
from django.forms import Textarea

# Django Autorizacion
from django.contrib.auth.models import User

# Models
from .models import Profile


class UsuarioCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UsuarioCreateForm, self).__init__(*args, **kwargs)
        self.fields['is_active'].initial = True

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'is_active',
            'is_staff',
        ]
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password': TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'Clave:',
            'first_name': 'Nombre:',
            'last_name': 'Apellidos:',
            'email': 'Email:',
            'password': 'Contraseña:',
            'is_active': 'Activo:',
            'is_staff': 'Administrador:',
        }


class UsuarioEditForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UsuarioEditForm, self).__init__(*args, **kwargs)
        self.fields['password'].required = False

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'is_active',
            'is_staff',
        ]
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password': TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'Nombre:',
            'last_name': 'Apellidos:',
            'email': 'Email:',
            'password': 'Contraseña:',
            'is_active': 'Activo:',
            'is_staff': 'Administrador:',
        }


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = [
            'user'
        ]
        widgets = {
            'puesto': TextInput(attrs={'class': 'form-control'}),
            'clave': TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': TextInput(attrs={'class': 'form-control'}),
            'comentarios': Textarea(attrs={'class': 'form-control'}),
        }
        # labels = {
        #     'first_name': 'Nombre:',
        #     'last_name': 'Apellidos:',
        #     'email': 'Email:',
        #     'password': 'Contraseña:',
        #     'is_active': 'Activo:',
        #     'is_staff': 'Administrador:',
        # }
