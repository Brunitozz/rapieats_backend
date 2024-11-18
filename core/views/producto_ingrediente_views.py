from rest_framework.viewsets import ModelViewSet
from core.models.producto_ingrediente import ProductoIngrediente
from core.serializers.producto_ingrediente_serializers import ProductoIngredienteSerializer

class ProductoIngredienteViewSet(ModelViewSet):
    queryset = ProductoIngrediente.objects.all()
    serializer_class = ProductoIngredienteSerializer
