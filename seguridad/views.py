# -*- coding: utf-8 -*-

# Librerias django

# Django Atajos
from django.shortcuts import render
from django.shortcuts import redirect

# Django Urls:
from django.core.urlresolvers import reverse

# # Django Login
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator

# Django Generic Views
from django.views.generic.base import View


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
