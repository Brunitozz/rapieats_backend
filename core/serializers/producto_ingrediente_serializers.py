from rest_framework import serializers
from core.models.producto_ingrediente import ProductoIngrediente

class ProductoIngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoIngrediente
        fields = '__all__'
