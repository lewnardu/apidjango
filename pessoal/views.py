from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response

from pessoal.models import (Cliente, Fornecedor, Funcionario, Pessoa,
                            PessoaFisica, PessoaJuridica)
from pessoal.serializers import (ClienteSerializer, FornecedorSerializer,
                                 FuncionarioSerializer, PessoaFisicaSerializer,
                                 PessoaJuridicaSerializer, PessoaSerializer)


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class PessoaFisicaViewSet(viewsets.ModelViewSet):
    queryset = PessoaFisica.objects.all()
    serializer_class = PessoaFisicaSerializer

class PessoaJuridicaViewSet(viewsets.ModelViewSet):
    queryset = PessoaJuridica.objects.all()
    serializer_class = PessoaJuridicaSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

