# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2024. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2024. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         30/01/24 13:53
# Project:      Zibanu - Django
# Module Name:  receivers
# Description:
# ****************************************************************
# Default imports
import inspect
import json

from django.forms.models import model_to_dict
from django.dispatch import receiver

from zibanu.django.lib import ExtendedJSONEncoder
from zibanu.django.logging.models import Log
from zibanu.django.logging.models import MailLog
from zibanu.django.utils import get_ip_address
from zibanu.django.utils import get_user
from zibanu.django.utils import get_request_from_stack
from .signals import send_mail


@receiver(send_mail)
def on_send_mail(sender, mail_from: str, mail_to: list, subject: str, smtp_error: str, smtp_code: int, **kwargs):
    """
    Event manager for send_mail signal

    Parameters
    ----------
    sender: Sender class of signal
    mail_from: Mail address from
    mail_to: Mail address list to
    subject: Subject of mail
    smtp_error: SMTP error string
    smtp_code: SMTP error code
    kwargs: Dictionary of parameters

    Returns
    -------
    None
    """
    smtp_error = None
    class_name = sender.__name__
    log = Log(sender=class_name, action=inspect.currentframe().f_code.co_name)
    log.save()
    mail_log = MailLog(log=log, mail_from=mail_from, mail_to=";".join(mail_to), subject=subject, smtp_error=smtp_error,
                       smtp_code=smtp_code)
    mail_log.save()


def audit_model(sender, action=None, **kwargs):
    """
    Receiver handler for audit models defined in EntityAudit model

    Parameters
    ----------
    sender : object: Sender class from receiver is call
    action : str: Audit action description
    kwargs : dict: Dictionary of parameters

    Returns
    -------
    None
    """
    # Get variables for Log
    model_name = sender._meta.app_label + "." + sender.__name__
    created = kwargs.get("created", False)
    instance = kwargs.get("instance")
    request = get_request_from_stack()
    user = get_user(request.user)
    ip_address = get_ip_address(request)

    if action != "on_delete":
        detail = {
            "new_values": model_to_dict(instance)
        }
    else:
        detail = {}

    if not created and instance is not None and hasattr(instance, "id"):
        try:
            old_values = sender.objects.get(pk=instance.id)
        except sender.DoesNotExist:
            old_values = None
        else:
            detail["old_values"] = model_to_dict(old_values)

    log = Log(sender=model_name, action=action, user=user, detail=json.dumps(detail, cls=ExtendedJSONEncoder),
              ip_address=ip_address)
    log.save()
