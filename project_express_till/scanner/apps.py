from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ScannerConfig(AppConfig):
    name = "project_express_till.scanner"
    verbose_name = _("Scanner")

