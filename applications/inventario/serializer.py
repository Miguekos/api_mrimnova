from rest_framework import serializers
from .models import ProductModel, ProveedoresModel, ServiceModel, FacturaModel

class ProveeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProveedoresModel
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaModel
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class ArrayIntegerSerializer(serializers.ListField):
    child = serializers.IntegerField()


class ArrayChartSerializer(serializers.ListField):
    child = serializers.CharField()


class ProductoSerializerNew(ProductoSerializer):
    serial_number = ArrayChartSerializer()
