from django.apps import AppConfig


class ProdutoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'produto'
default_app_config = 'produto.apps.ProdutoConfig'