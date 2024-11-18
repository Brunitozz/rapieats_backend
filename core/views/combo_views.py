from rest_framework.viewsets import ModelViewSet
from core.models.combo import Combo, ComboProducto
from core.serializers.combo_serializers import ComboSerializer, ComboProductoSerializer

class ComboViewSet(ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer

class ComboProductoViewSet(ModelViewSet):
    queryset = ComboProducto.objects.all()
    serializer_class = ComboProductoSerializer
