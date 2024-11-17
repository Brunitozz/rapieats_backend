from rest_framework import serializers
from core.models.combo import Combo, ComboProducto

class ComboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = '__all__'


class ComboProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComboProducto
        fields = '__all__'
