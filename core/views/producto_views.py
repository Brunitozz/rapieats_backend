from rest_framework.viewsets import ModelViewSet
from core.models.producto import Producto, Categoria, Ingrediente
from core.serializers.producto_serializers import ProductoSerializer, CategoriaSerializer, IngredienteSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class IngredienteViewSet(ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
