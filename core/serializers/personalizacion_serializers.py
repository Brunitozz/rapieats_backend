from rest_framework import serializers
from core.models.personalizacion import Personalizacion, DetalleAdicional

class PersonalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personalizacion
        fields = '__all__'


class DetalleAdicionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleAdicional
        fields = '__all__'
