# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         8/11/23 22:19
# Project:      Zibanu - Django
# Module Name:  service_not_implemented
# Description:
# ****************************************************************
# Default imports
import logging
import traceback
from django.utils.translation import gettext_lazy as _
from .api_exception import APIException
from rest_framework import status

class APINotImplementedException(APIException):
    status_code = status.HTTP_405_METHOD_NOT_ALLOWED
    default_detail = _("Service not implemented")
    default_code = "not_implemented"