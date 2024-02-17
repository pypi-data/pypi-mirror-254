from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HaalCentraalHRApp(AppConfig):
    name = "prefill_haalcentraalhr"
    label = "prefill_haalcentraalhr"
    verbose_name = _("Haal Centraal HR")

    def ready(self):
        from . import plugin  # noqa
