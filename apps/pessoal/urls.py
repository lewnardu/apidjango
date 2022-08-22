from django.urls import include, path
from rest_framework import routers

from pessoal.views import (ClienteViewSet, FornecedorViewSet,
                           FuncionarioViewSet, PessoaFisicaViewSet,
                           PessoaJuridicaViewSet, PessoaViewSet)

router = routers.DefaultRouter()

#router.register(r'pessoas', PessoaViewSet)
#router.register(r'pessoafisicas', PessoaFisicaViewSet)
#router.register(r'pessoajuridicas', PessoaJuridicaViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'fornecedores', FornecedorViewSet)
router.register(r'clientes', ClienteViewSet)
app_name = 'pessoal'
urlpatterns = [
    path("", include(router.urls)),
]