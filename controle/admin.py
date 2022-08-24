from django.contrib import admin

from controle.models import FormaPagamento, Pedido, ProdutoPedido


@admin.register(FormaPagamento)
class FormaPagamentoAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(ProdutoPedido)
class ProdutoPedidoAdmin(admin.ModelAdmin):
    exclude = ()

