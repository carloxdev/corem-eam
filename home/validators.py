# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError


def valid_extension(value):
    if (not value.name.endswith('.png') and
        not value.name.endswith('.jpeg') and
            not value.name.endswith('.jpg')):

        raise ValidationError("Archivos permitidos: .jpg, .jpeg, .png")


def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 2.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError("Tamaño Máximo de Archivo %sMB" %
                              str(megabyte_limit))
