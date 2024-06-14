from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'


class SuitConfig(DjangoSuitConfig):
    layout='horizontal'