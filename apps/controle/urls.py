from django.urls import include, path
from rest_framework import routers

from controle.views import (FormaPagamentoViewSet, PedidoViewSet,
                            ProdutoPedidoViewSet)

router = routers.DefaultRouter()

router.register(r'formaspagamento', FormaPagamentoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'produtospedidos', ProdutoPedidoViewSet)
app_name = 'controle'
urlpatterns = [
    path("", include(router.urls)),
]