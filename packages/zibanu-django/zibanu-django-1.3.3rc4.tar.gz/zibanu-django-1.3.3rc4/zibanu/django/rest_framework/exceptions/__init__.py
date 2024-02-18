# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         13/12/22 1:15 PM
# Project:      Zibanu Django Project
# Module Name:  __init__.py
# Description:
# ****************************************************************
from .api_exception import APIException
from .multiple_login_error import MultipleLoginError
from .api_not_implemented_exception import APINotImplementedException
from rest_framework.exceptions import ValidationError, PermissionDenied, ParseError, UnsupportedMediaType
from rest_framework.exceptions import NotFound, AuthenticationFailed, MethodNotAllowed, NotAcceptable

__all__ = [
    "AuthenticationFailed",
    "APIException",
    "MethodNotAllowed",
    "MultipleLoginError",
    "NotAcceptable",
    "NotFound",
    "ParseError",
    "PermissionDenied",
    "APINotImplementedException",
    "UnsupportedMediaType",
    "ValidationError",
]
