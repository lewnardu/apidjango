from django.contrib import admin

from utilidades.models import Contato, Endereco


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    exclude = ()

