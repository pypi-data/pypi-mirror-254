# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2024. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2024. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         30/01/24 12:34
# Project:      Zibanu - Django
# Module Name:  admin
# Description:
# ****************************************************************
# Default imports
import logging
import traceback
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from zibanu.django.logging.admin_views import AuditEntityAdmin
from zibanu.django.logging.models import AuditEntity

admin.site.register(AuditEntity, AuditEntityAdmin)