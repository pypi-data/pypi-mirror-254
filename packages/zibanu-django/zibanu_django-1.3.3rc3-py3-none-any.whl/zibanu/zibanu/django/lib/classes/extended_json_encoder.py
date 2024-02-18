# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2024. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2024. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         30/01/24 16:08
# Project:      Zibanu - Django
# Module Name:  extended_json_encoder
# Description:
# ****************************************************************
# Default imports
import datetime

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.files import FileField, ImageFieldFile


class ExtendedJSONEncoder(DjangoJSONEncoder):
    """
    Extended JSON encoder for Django models that use ImageField, FileField and DateTimeField
    """

    def default(self, o):
        if isinstance(o, FileField) or isinstance(o, ImageFieldFile):
            return str(o)
        elif isinstance(o, datetime.datetime):
            return o.strftime('%Y-%M-%d %H:%M:%S')
        elif isinstance(o, datetime.date):
            return o.strftime('%Y-%m-%d')
        else:
            return super().default(o)
