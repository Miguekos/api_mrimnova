from rest_framework import serializers
from .models import ClientModel, ProductModel, ServiceModel


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
    type_document_name = serializers.CharField(
        source='get_type_document_display', read_only=True
    )

    class Meta:
        model = ClientModel
        fields = (
            'name',
            'address_main',
            'email',
            'type_document',
            'type_document_name',
            'document',
            'date_received'
        )

    # def get_type_method_products(self, obj):
    #     return obj.get_type_method_products_display()

    # def get_type_method_services(self, obj):
    #     return obj.get_type_method_services_display()
    #
    # def get_type_document(self, obj):
    #     return obj.get_type_document_display()


class ClientSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = ('__all__')
