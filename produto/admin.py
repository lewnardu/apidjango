from django.contrib import admin

from produto.models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    exclude = ()

