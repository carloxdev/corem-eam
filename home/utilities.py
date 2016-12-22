# -*- coding: utf-8 -*-

import os


def get_ImagePath(instance, filename):
    upload_dir = os.path.join('equipos', 'anexos', 'img')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)


def get_FilePath(instance, filename):
    upload_dir = os.path.join('equipos', 'anexos', 'files')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)
