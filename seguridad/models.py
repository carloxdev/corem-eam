# -*- coding: utf-8 -*-

# Librerias Django:
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Django Signals:
from django.db.models.signals import post_save
from django.dispatch import receiver

# Otros modelos:
from home.validators import valid_extension
from home.validators import validate_image


class Empresa(models.Model):

    clave = models.CharField(max_length=144, null=True)
    descripcion = models.CharField(max_length=144, null=True)
    logo = models.ImageField(
        upload_to='empresas/img/',
        blank=True,
        null=True,
        validators=[
            valid_extension,
            validate_image
        ]
    )

    def __str__(self):
        return self.clave.encode('utf-8')


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puesto = models.CharField(
        max_length=144,
        null=True,
        blank=True
    )
    clave = models.CharField(
        max_length=144,
        null=True,
        blank=True
    )
    fecha_nacimiento = models.DateField(null=True, blank=True)
    imagen = models.ImageField(
        upload_to='usuarios/img/',
        blank=True,
        null=True,
        validators=[
            valid_extension,
            validate_image
        ]
    )
    costo = models.DecimalField(
        max_digits=20, decimal_places=4, default=0.0, blank=True, null=True
    )
    comentarios = models.TextField(max_length=500, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
