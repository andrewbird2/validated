# -*- coding: utf-8
from django.apps import AppConfig


class ValidatedConfig(AppConfig):
    name = 'validated'

    def ready(self):
        from .registry import get_model_tests
        get_model_tests()
