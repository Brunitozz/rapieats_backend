from rest_framework.viewsets import ModelViewSet
from core.models.personalizacion import Personalizacion, DetalleAdicional
from core.serializers.personalizacion_serializers import PersonalizacionSerializer, DetalleAdicionalSerializer

class PersonalizacionViewSet(ModelViewSet):
    queryset = Personalizacion.objects.all()
    serializer_class = PersonalizacionSerializer

class DetalleAdicionalViewSet(ModelViewSet):
    queryset = DetalleAdicional.objects.all()
    serializer_class = DetalleAdicionalSerializer
