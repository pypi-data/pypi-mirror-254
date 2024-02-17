# -*- coding: utf-8 -*-

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         16/03/23 10:36
# Project:      Zibanu Django Project
# Module Name:  signals
# Description:
# ****************************************************************
import inspect
from django import dispatch


send_mail = dispatch.Signal()

