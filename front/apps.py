# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class FrontConfig(AppConfig):
    name = 'front'

    def ready(self):
        import front.signals
