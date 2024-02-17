# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         10/12/22 10:23 AM
# Project:      Zibanu Django Project
# Module Name:  apps
# Description:
# ****************************************************************
import logging

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ZbDjangoLogging(AppConfig):
    """
    Inherited class from django.apps.AppConfig to define configuration of zibanu.django.logging app.
    """
    default_auto_field = "django.db.models.AutoField"
    name = "zibanu.django.logging"
    verbose_name = _("Zibanu Logging")
    label = "zb_logging"

    def ready(self):
        """
        Override method used for django application loader after the application has been loaded successfully.
        """
        # Import events for signals
        self.handler_factory()

    def handler_factory(self):
        """
        Method to create a signals connections between handlers and entities stored in EntityAudit

        Returns
        -------
        None
        """
        from functools import partial
        from django.apps import apps
        from django.db.models.signals import pre_save, post_save, post_delete
        from zibanu.django.lib import ModelName
        from zibanu.django.logging.lib.receivers import audit_model
        try:
            from zibanu.django.logging.models import AuditEntity

            qs_audit_entity = AuditEntity.objects.filter(enabled__exact=True).all()
            for entity in qs_audit_entity:
                model_name = ModelName(entity.model_name)
                model = apps.get_model(model_name.app_label, model_name.model_name)

                if entity.on_create:
                    post_save.connect(partial(audit_model, action="on_create"), sender=model)

                if entity.on_update:
                    pre_save.connect(partial(audit_model, action="on_update"), sender=model)

                if entity.on_delete:
                    post_delete.connect(partial(audit_model, action="on_delete"), sender=model)
        except ImportError:
            logging.info(_("Unable to import AuditEntity model"))
        except Exception as exc:
            logging.info(str(exc))
