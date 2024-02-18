from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class PpmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PPM'
    verbose_name = _("Private Package Manager")
