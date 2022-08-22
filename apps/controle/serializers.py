from rest_framework import serializers

from controle.models import FormaPagamento, Pedido, ProdutoPedido


class FormaPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPagamento
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class ProdutoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoPedido
        fields = '__all__'

