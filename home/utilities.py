# -*- coding: utf-8 -*-

import os


def get_ImagePath(instance, filename):
    if (instance.equipo_id):
        upload_dir = os.path.join(
            'equipos', instance.equipo_id, 'anexos', 'img')
    elif (instance.articulo_id):
        upload_dir = os.path.join(
            'articulos', instance.articulo_id, 'anexos', 'img')
    return os.path.join(upload_dir, filename)


def get_FilePath(instance, filename):
    if (instance.equipo_id):
        upload_dir = os.path.join(
            'equipos', instance.equipo_id, 'anexos', 'files')
    elif (instance.articulo_id):
        upload_dir = os.path.join(
            'articulos', instance.articulo_id, 'anexos', 'files')
    return os.path.join(upload_dir, filename)
