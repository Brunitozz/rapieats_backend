from rest_framework import serializers
from payments.models import Pago

class PagoSerializer(serializers.ModelSerializer):
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)

    class Meta:
        model = Pago
        fields = ['id_pago', 'metodo', 'monto', 'estado', 'estado_display']
        read_only_fields = ['id_pago']
