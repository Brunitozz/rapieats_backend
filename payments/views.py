from rest_framework.viewsets import ModelViewSet
from payments.models import Pago
from payments.serializers import PagoSerializer

class PagoViewSet(ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

    def perform_create(self, serializer):
        """Personaliza el comportamiento en la creación de un pago."""
        serializer.save()

    def perform_update(self, serializer):
        """Personaliza el comportamiento en la actualización de un pago."""
        serializer.save()
