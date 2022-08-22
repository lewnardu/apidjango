from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response

from utilidades.models import Contato, Endereco
from utilidades.serializers import ContatoSerializer, EnderecoSerializer


class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

