from django.db import models
from configuracao.models import SoftDeletionModel
from utilidades.models import Contato, Endereco

class Pessoa(SoftDeletionModel):    
    nome = models.CharField(max_length=255, null=True, blank=True)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE, null=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} {self.contato} {self.endereco}"

    class Meta:
        verbose_name_plural = "Pessoas"

class PessoaFisica(Pessoa):    
    nome_social = models.CharField(max_length=255, null=True, blank=True)
    cpf = models.CharField(max_length=255, null=True, blank=True)
    rg = models.CharField(max_length=255, null=True, blank=True)
    sexo = models.CharField(max_length=255, null=True, blank=True)
    data_nascimento = models.DateField()

    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"{self.nome_social} {self.cpf} {self.rg} {self.sexo} {self.data_nascimento}"

    class Meta:
        verbose_name_plural = "Pessoas Físicas"

class PessoaJuridica(Pessoa):    
    razao_social = models.CharField(max_length=255, null=True, blank=True)
    cnpj = models.CharField(max_length=255, null=True, blank=True)
   
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"{self.razao_social} {self.cnpj}"

    class Meta:
        verbose_name_plural = "Pessoas Jurídicas"

class Funcionario(PessoaFisica):    
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f""

    class Meta:
        verbose_name_plural = "Funcionários"

class Fornecedor(PessoaJuridica):    
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f""

    class Meta:
        verbose_name_plural = "Fornecedores"

class Cliente(PessoaFisica):      
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f""

    class Meta:
        verbose_name_plural = "Clientes"

