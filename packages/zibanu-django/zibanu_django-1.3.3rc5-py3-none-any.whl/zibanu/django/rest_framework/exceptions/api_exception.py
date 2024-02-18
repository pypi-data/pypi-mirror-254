# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         14/12/22 4:14 AM
# Project:      Zibanu Django Project
# Module Name:  api_exception
# Description:
# ****************************************************************
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException as SourceException


class APIException(SourceException):
    """
    Inherited class from rest_framework.exceptions.ApiException
    """
    __default_messages = {
        "304": _("Object has not been created."),
        "400": _("Generic error."),
        "401": _("You are not authorized for this resource."),
        "403": _("You do not have permission to perform this action."),
        "404": _("Object does not exists."),
        "406": _("Data validation error."),
        "412": _("Data required not found."),
        "500": _("Not controlled exception error. Please contact administrator."),
    }

    __default_codes = {
        "304": "object_not_created",
        "400": "error",
        "401": "unauthorized",
        "403": "forbidden",
        "404": "not_found",
        "406": "validation_error",
        "412": "precondition_failed",
        "500": "not_controlled_exception"
    }

    def __init__(self, detail: str = None, code: str = None, status_code: int = None, **kwargs) -> None:
        """
        Constructor method

        Parameters
        ----------
        detail : str: String message to be sent through exception.
        code : str: String exception code to be sent through exception.
        http_status: int: HTTP Status code
        msg: Message to send trough exception. (Legacy)
        error: Error code or long description. (Legacy)
        """
        if status_code is not None:
            self.status_code = status_code
        else:
            self.status_code = kwargs.get("http_status", 500)

        str_status_code = str(self.status_code)

        # Set default detail
        # TODO: Optimize procedure
        if detail is not None:
            if isinstance(detail, (list, tuple)):
                self.default_detail = detail[0]
            elif isinstance(detail, dict):
                self.default_detail = ""
                for key, value in detail.items():
                    self.default_detail += key + ": "
                    if isinstance(value, (list, tuple)):
                        for item in value:
                            self.default_detail += item + ";"
                        self.default_detail = self.default_detail[:-1]
                    else:
                        self.default_detail += value
            else:
                self.default_detail = detail
        elif "msg" in kwargs:
            self.default_detail = kwargs.get("msg")
        else:
            if str_status_code in self.__default_messages:
                self.default_detail = self.__default_messages.get(str_status_code)

        # Set default code
        if code is not None:
            self.default_code = code
        elif "error" in kwargs:
            self.default_code = kwargs.get("error")
        else:
            if str_status_code in self.__default_codes:
                self.default_code = self.__default_codes.get(str_status_code)

        super().__init__()
