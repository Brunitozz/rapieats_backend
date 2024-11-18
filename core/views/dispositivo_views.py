from rest_framework.viewsets import ModelViewSet
from core.models.dispositivo import DispositivoDeAutoservicio
from core.serializers.dispositivo_serializers import DispositivoSerializer

class DispositivoViewSet(ModelViewSet):
    queryset = DispositivoDeAutoservicio.objects.all()
    serializer_class = DispositivoSerializer
