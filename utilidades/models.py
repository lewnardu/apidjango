from django.db import models
from configuracao.models import SoftDeletionModel

class Contato(SoftDeletionModel):    
    telefone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=254)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.telefone} {self.email}"

    class Meta:
        verbose_name_plural = "Contatos"

class Endereco(SoftDeletionModel):    
    cep = models.CharField(max_length=255, null=True, blank=True)
    logradouro = models.CharField(max_length=255, null=True, blank=True)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.CharField(max_length=255, null=True, blank=True)
    localidade = models.CharField(max_length=255, null=True, blank=True)
    uf = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cep} {self.logradouro} {self.complemento} {self.bairro} {self.localidade} {self.uf}"

    class Meta:
        verbose_name_plural = "Endereços"

