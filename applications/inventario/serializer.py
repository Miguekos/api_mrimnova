from rest_framework import serializers
from datetime import timedelta
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
    proveedor_name = serializers.SerializerMethodField()
    created_parse = serializers.SerializerMethodField()

    class Meta:
        model = FacturaModel
        fields = [
            'id',
            'created',
            'created_parse',
            'modified',
            'type_invoice',
            'codigo',
            'proveedor',
            'proveedor_name',
            'id_invoice'
        ]

    def get_id_invoice(self, obj):
        return obj.id

    def get_proveedor_name(self, obj):
        return obj.proveedor.name

    def get_created_parse(self, obj):
        return "{}".format((obj.created - timedelta(hours=5)).strftime("%d/%m/%Y, %H:%M"))


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
