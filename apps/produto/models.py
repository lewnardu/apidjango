from django.db import models
from configuracao.models import SoftDeletionModel

class Categoria(SoftDeletionModel):    
    nome = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} {self.descricao}"

    class Meta:
        verbose_name_plural = "Categorias"

class Produto(SoftDeletionModel):    
    nome = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    preco_custo = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=0.0)
    preco_venda = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=0.0)
    status_inventario = models.BooleanField()
    avaliacao = models.CharField(max_length=255, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} {self.descricao} {self.preco_custo} {self.preco_venda} {self.status_inventario} {self.avaliacao} {self.categoria}"

    class Meta:
        verbose_name_plural = "Produtos"

