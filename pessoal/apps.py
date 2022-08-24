from django.apps import AppConfig


class PessoalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pessoal'
default_app_config = 'pessoal.apps.PessoalConfig'

