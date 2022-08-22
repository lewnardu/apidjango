from django.urls import include, path
from rest_framework import routers

from produto.views import CategoriaViewSet, ProdutoViewSet

router = routers.DefaultRouter()

router.register(r'categorias', CategoriaViewSet)
router.register(r'produtos', ProdutoViewSet)
app_name = 'produto'
urlpatterns = [
    path("", include(router.urls)),
]