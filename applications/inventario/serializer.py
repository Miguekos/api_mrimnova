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
    id_invoice = serializers.SerializerMethodField()

    class Meta:
        model = FacturaModel
        fields = (
            'id',
            'created',
            'modified',
            'type_invoice',
            'codigo',
            'proveedor',
            'id_invoice'
        )

    def get_id_invoice(self, obj):
        return obj.id


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
