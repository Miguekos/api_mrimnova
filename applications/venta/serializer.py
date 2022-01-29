from rest_framework import serializers
from .models import ClientModel, ProductModel, ServiceModel, VentasModelo

from applications.basededatos.serializer import ClientSerializerPost
from applications.inventario.serializer import ProductoSerializer


class VentasSerializer(serializers.ModelSerializer):
    client = ClientSerializerPost()
    products = ProductoSerializer(many=True)
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
            "quote",
            "products"
        ]

class VentasSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = VentasModelo
        fields = ('__all__')
