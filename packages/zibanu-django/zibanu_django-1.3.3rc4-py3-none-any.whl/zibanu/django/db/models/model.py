# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         13/12/22 10:14 AM
# Project:      Zibanu Django Project
# Module Name:  base_model
# Description:
# ****************************************************************
from django.db import models


class Model(models.Model):
    """
    Inherited abstract class from models.Model to add the "use_db" attribute.
    """
    # Protected attribute
    use_db = "default"

    def set(self, fields: dict, force_update: bool = True):
        """
        Method to save a set of fields from a dictionary.

        Parameters
        ----------
        force_update : bool, optional: Flag to force update of the user profile. Defaults to True
        fields: Dictionary with fields keys and values.

        Returns
        -------
        None
        """
        force_insert = not force_update
        for key, value in fields.items():
            if hasattr(self, key):
                setattr(self, key, value)
            self.save(force_update=force_update, force_insert=force_insert)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Override method to save the model forcing full clean.

        Parameters
        ----------
        force_insert : force insert record instead of updating it
        force_update : force update record instead of insert it
        using : setting db name to user
        update_fields : list of fields to be updated

        Returns
        -------
        None
        """
        self.full_clean()
        return super().save(force_insert=force_insert, force_update=force_update, using=using,
                            update_fields=update_fields)

    class Meta:
        """
        Metaclass for Model class.
        """
        abstract = True
