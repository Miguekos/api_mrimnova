from rest_framework import serializers
from .models import ClientModel, ProductModel, ServiceModel
from applications.venta.models import VentasModelo


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class ServiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = ('__all__')


class ClientSerializer(serializers.ModelSerializer):
    # products = ProductModelSerializer(many=True)
    # services = ServiceModelSerializer(many=True)
    # type_method_products = serializers.SerializerMethodField()
    # type_method_products_name = serializers.CharField(
    #     source='get_type_method_products_display', read_only=True
    # )
    # type_method_services_name = serializers.CharField(
    #     source='get_type_method_services_display', read_only=True
    # )
    monitoreos = serializers.SerializerMethodField()
    type_document_name = serializers.CharField(
        source='get_type_document_display', read_only=True
    )

    class Meta:
        model = ClientModel
        fields = (
            'id',
            'name',
            'address_main',
            'email',
            'type_document',
            'type_document_name',
            'document',
            'profile',
            'date_received',
            'monitoreos'
        )

    def get_monitoreos(self, obj):
        return VentasSerializerMonitoreo(
            VentasModelo.objects.get_sales_for_id(obj.id),
            many=True
        ).data


class ClientSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = ('__all__')


class VentasSerializerMonitoreo(serializers.ModelSerializer):
    type_sales_name = serializers.CharField(
        source='get_type_sales_display', read_only=True
    )

    class Meta:
        model = VentasModelo
        fields = [
            'id',
            'type_sales',
            'type_sales_name',
            'contracts',
            'address',
            "details",
            "descriptions",
            "materials",
            "cost",
            "quote"
        ]
