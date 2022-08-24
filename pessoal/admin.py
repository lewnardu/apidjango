from django.contrib import admin

from pessoal.models import (Cliente, Fornecedor, Funcionario, Pessoa,
                            PessoaFisica, PessoaJuridica)


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(PessoaJuridica)
class PessoaJuridicaAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    exclude = ()

