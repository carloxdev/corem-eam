# -*- coding: utf-8 -*-

# API Rest
from rest_framework.pagination import PageNumberPagination


class GenericPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
