from django.apps import AppConfig


class ConfiguracaoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'configuracao'
default_app_config = 'configuracao.apps.ConfiguracaoConfig'
