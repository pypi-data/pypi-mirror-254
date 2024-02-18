# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         10/12/22 10:27 AM
# Project:      Zibanu Django Project
# Module Name:  models
# Description:
# ****************************************************************
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from zibanu.django.db import models


class Log(models.DatedModel):
    """
    Model for storing log events
    """
    action = models.CharField(max_length=100, blank=False, null=False, verbose_name=_("Action"))
    sender = models.CharField(max_length=100, blank=False, null=False, verbose_name=_("Sender object method"))
    detail = models.TextField(max_length=200, blank=True, null=False, default="", verbose_name=_("Log detail"))
    ip_address = models.GenericIPAddressField(blank=True, null=True, verbose_name=_("IP Address"))
    user = models.ForeignKey(get_user_model(), null=True, blank=True, verbose_name=_("User"), on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=("user",), name="IDX_logging_log_user"),
            models.Index(fields=("action",), name="IDX_logging_log_action")
        ]


class MailLog(models.Model):
    """
    Model to store mail logging status answers
    """
    log = models.OneToOneField(Log, blank=False, null=False, on_delete=models.PROTECT, verbose_name=_("Log"))
    mail_from = models.CharField(max_length=250, blank=False, null=False, verbose_name=_("Mail From"))
    mail_to = models.CharField(max_length=250, blank=False, null=False, verbose_name=_("Mail To"))
    subject = models.CharField(max_length=250, blank=False, null=False, verbose_name=_("Subject"))
    smtp_code = models.IntegerField(blank=False, null=False, verbose_name=_("SMTP Code"), default=0)
    smtp_error = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("SMTP Error"))


class AuditEntity(models.Model):
    """
    Model to define entities to be logged in
    """
    model_name = models.CharField(max_length=250, blank=False, null=False, verbose_name=_("Model Name"),
                                  help_text=_("The name of the model you would like to audit"))
    on_create = models.BooleanField(default=False, verbose_name=_("On Insert"),
                                    help_text=_("If true, this entity will be audited on insert event"))
    on_delete = models.BooleanField(default=False, verbose_name=_("On Delete"),
                                    help_text=_("If true, this entity will be audited on delete event"))
    on_update = models.BooleanField(default=False, verbose_name=_("On Update"),
                                    help_text=_("If true, this entity will be audited on update event"))
    enabled = models.BooleanField(default=True, verbose_name=_("Enabled"),
                                  help_text=_("If false, disable the audit rule"))

    def __str__(self):
        return self.model_name

    class Meta:
        verbose_name = _("Audit Entity")
        verbose_name_plural = _("Audit Entities")
        ordering = ["model_name"]
        unique_together = ("model_name",)
