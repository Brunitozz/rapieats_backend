from rest_framework import serializers
from core.models.dispositivo import DispositivoDeAutoservicio

class DispositivoDeAutoservicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispositivoDeAutoservicio
        fields = '__all__'
