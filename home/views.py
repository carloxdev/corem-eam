# -*- coding: utf-8 -*-

# Librerias django

# Django Atajos
from django.shortcuts import render

# Django Generic Views
from django.views.generic.base import View


class Index(View):

    def __init__(self):
        self.template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        return render(request, self.template_name, {})
