from rest_framework import viewsets
from core.models.combo import Combo, ComboProducto
from core.serializers.combo_serializers import ComboSerializer, ComboProductoSerializer

class ComboViewSet(viewsets.ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer


class ComboProductoViewSet(viewsets.ModelViewSet):
    queryset = ComboProducto.objects.all()
    serializer_class = ComboProductoSerializer
