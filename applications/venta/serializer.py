from rest_framework import serializers
from .models import ClientModel, ProductModel, ServiceModel, VentasModelo

from applications.basededatos.serializer import ClientSerializerPost


class VentasSerializer(serializers.ModelSerializer):
    client = ClientSerializerPost()
    type_sales_name = serializers.CharField(
        source='get_type_sales_display', read_only=True
    )

    class Meta:
        model = VentasModelo
        fields = [
            'id',
            'client',
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


class VentasSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = VentasModelo
        fields = ('__all__')
