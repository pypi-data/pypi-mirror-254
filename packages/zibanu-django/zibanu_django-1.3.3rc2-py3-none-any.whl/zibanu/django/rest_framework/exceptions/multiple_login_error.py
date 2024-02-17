# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         8/11/23 06:13
# Project:      Zibanu - Django
# Module Name:  validation_error
# Description:
# ****************************************************************
# Default imports
from .api_exception import APIException
from rest_framework import status



class MultipleLoginError(APIException):
    """
    Override class for ValidationError
    """
    status_code = status.HTTP_412_PRECONDITION_FAILED
    default_code = "multiple_login"
