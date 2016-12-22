# -*- coding: utf-8 -*-

# Librerias Django:
from __future__ import unicode_literals
from django.db import models


class Empresa(models.Model):

    clave = models.CharField(max_length=144, null=True)
    descripcion = models.CharField(max_length=144, null=True)
    logo = models.ImageField(upload_to='empresas', blank=True, null=True)

    def __str__(self):
        return self.clave.encode('utf-8')
