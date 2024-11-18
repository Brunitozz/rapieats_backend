from rest_framework.viewsets import ModelViewSet
from core.models.pedido import Pedido, DetallePedido
from core.serializers.pedido_serializers import PedidoSerializer, DetallePedidoSerializer

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class DetallePedidoViewSet(ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
