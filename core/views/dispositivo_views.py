from rest_framework import viewsets
from core.models.dispositivo import DispositivoDeAutoservicio
from core.serializers.dispositivo_serializers import DispositivoDeAutoservicioSerializer

class DispositivoDeAutoservicioViewSet(viewsets.ModelViewSet):
    queryset = DispositivoDeAutoservicio.objects.all()
    serializer_class = DispositivoDeAutoservicioSerializer
