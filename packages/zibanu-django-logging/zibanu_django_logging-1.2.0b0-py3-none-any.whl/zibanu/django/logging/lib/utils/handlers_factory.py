# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2024. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2024. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         1/02/24 11:42
# Project:      Zibanu - Django
# Module Name:  handlers_factory
# Description:
# ****************************************************************
# Default imports
import logging
import uuid

from django.utils.translation import gettext_lazy as _


def handlers_factory(model=None, delete: bool = False):
    """
    Script to create handlers for post_save and post_delete signals and logging it.

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
        if model is not None and isinstance(model, AuditEntity):
            qs_audit_entity = AuditEntity.objects.filter(model_name__iexact=model.model_name)
        else:
            qs_audit_entity = AuditEntity.objects.filter(enabled__exact=True).all()

        for entity in qs_audit_entity:
            model_name = ModelName(entity.model_name)
            model = apps.get_model(model_name.app_label, model_name.model_name)
            # Disconnect previous signals
            post_save.disconnect(audit_model, sender=model)
            pre_save.disconnect(audit_model, sender=model)
            post_delete.disconnect(audit_model, sender=model)

            if not delete:
                if entity.on_create:
                    post_save.connect(partial(audit_model, action="on_create"), sender=model,
                                      dispatch_uid=uuid.uuid4().hex)

                if entity.on_update:
                    pre_save.connect(partial(audit_model, action="on_update"), sender=model,
                                     dispatch_uid=uuid.uuid4().hex)

                if entity.on_delete:
                    post_delete.connect(partial(audit_model, action="on_delete"), sender=model,
                                        dispatch_uid=uuid.uuid4().hex)
    except ImportError:
        logging.info(_("Unable to import AuditEntity model"))
    except Exception as exc:
        logging.info(str(exc))
