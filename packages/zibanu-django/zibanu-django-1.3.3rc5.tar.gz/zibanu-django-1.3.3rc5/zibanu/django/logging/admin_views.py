# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2024. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2024. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         30/01/24 11:46
# Project:      Zibanu - Django
# Module Name:  admin_views
# Description:
# ****************************************************************
# Default imports
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.forms import Select

from zibanu.django.logging.lib import handlers_factory
from zibanu.django.utils import get_model_list

MODEL_LIST_CHOICES = tuple(zip(get_model_list(), get_model_list()))


class AuditEntityAdmin(admin.ModelAdmin):
    actions = None
    list_display = ("model_name", "enabled")
    fieldsets = (
        (None, {"fields": ("model_name",)}),
        (_("Actions"), {"fields": ("on_create", "on_update", "on_delete")}),
        (None, {"fields": ("enabled",)})
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super(AuditEntityAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields["model_name"].widget = Select(choices=MODEL_LIST_CHOICES)
        return form

    def save_model(self, request, obj, form, change):
        handlers_factory()
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        handlers_factory(model=obj, delete=True)
        super().delete_model(request, obj)
