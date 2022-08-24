from django.urls import include, path
from rest_framework import routers

from utilidades.views import ContatoViewSet, EnderecoViewSet

router = routers.DefaultRouter()

router.register(r'contatos', ContatoViewSet)
router.register(r'enderecos', EnderecoViewSet)
app_name = 'utilidades'
urlpatterns = [
    path("", include(router.urls)),
]