# -*- coding: utf-8 -*-

# Librerias Django
from django.forms import ModelForm
from django.forms import EmailInput
from django.forms import TextInput

# Django Autorizacion
from django.contrib.auth.models import User


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
            'username': 'Clave:',
            'first_name': 'Nombre:',
            'last_name': 'Apellidos:',
            'email': 'Email:',
            'password': 'Contraseña:',
            'is_active': 'Activo:',
            'is_staff': 'Administrador:',
        }
