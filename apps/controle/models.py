from django.db import models
from configuracao.models import SoftDeletionModel
from pessoal.models import Funcionario, Cliente
from produto.models import Produto

class FormaPagamento(SoftDeletionModel):    
    nome = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} {self.descricao}"

    class Meta:
        verbose_name_plural = "Formas de pagamento"

class Pedido(SoftDeletionModel):    
    data = models.DateField()
    frete = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=0.0)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.data} {self.frete} {self.funcionario} {self.cliente} {self.forma_pagamento}"

    class Meta:
        verbose_name_plural = "Pedidos"

class ProdutoPedido(SoftDeletionModel):    
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    quantidade = models.PositiveIntegerField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pedido} {self.produto} {self.quantidade} {self.desconto}"

    class Meta:
        verbose_name_plural = "Produtos Pedidos"

