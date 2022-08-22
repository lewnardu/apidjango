from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response

from controle.models import FormaPagamento, Pedido, ProdutoPedido
from controle.serializers import (FormaPagamentoSerializer, PedidoSerializer,
                                  ProdutoPedidoSerializer)


class FormaPagamentoViewSet(viewsets.ModelViewSet):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ProdutoPedidoViewSet(viewsets.ModelViewSet):
    queryset = ProdutoPedido.objects.all()
    serializer_class = ProdutoPedidoSerializer

