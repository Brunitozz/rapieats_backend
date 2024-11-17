from rest_framework import viewsets
from core.models.personalizacion import Personalizacion, DetalleAdicional
from core.serializers.personalizacion_serializers import PersonalizacionSerializer, DetalleAdicionalSerializer

class PersonalizacionViewSet(viewsets.ModelViewSet):
    queryset = Personalizacion.objects.all()
    serializer_class = PersonalizacionSerializer


class DetalleAdicionalViewSet(viewsets.ModelViewSet):
    queryset = DetalleAdicional.objects.all()
    serializer_class = DetalleAdicionalSerializer
