from rest_framework import serializers
from datetime import timedelta
from .models import ClientModel, ProductModel, ServiceModel, VentasModelo

from applications.basededatos.serializer import ClientSerializerPost
from applications.inventario.serializer import ProductoSerializer


class VentasSerializer(serializers.ModelSerializer):
    client = ClientSerializerPost()
    products = ProductoSerializer(many=True)
    date_received_parse = serializers.SerializerMethodField()
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
            "products",
            "type_method_products",
            "down_payment_producto_cre",
            "quotas_producto_cre",
            "services",
            "type_method_services",
            "down_payment_servicios_cre",
            "quotas_servicios_cre",
            "bills_receivable",
            "payment_notifications",
            "date_received",
            "date_received_parse",
        ]

    def get_date_received_parse(self, obj):
        return "{}".format((obj.date_received - timedelta(hours=5)).strftime("%d/%m/%Y, %H:%M"))


class VentasSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = VentasModelo
        fields = ('__all__')


class VentasSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = VentasModelo
        fields = (
            'client',
            'type_sales',
            'contracts',
            'address',
            'products',
            'type_method_products',
            'down_payment_producto_cre',
            'quotas_producto_cre',
            'services',
            'type_method_services',
            'down_payment_servicios_cre',
            'quotas_servicios_cre',
            'bills_receivable',
            'payment_notifications',
            'details',
            'descriptions',
            'materials',
            'cost',
            'quote',
            'date_received',
        )

        # class Meta:
        #     products = Nuevoobjeto


class DictValidate(serializers.Serializer):
    id_pro = serializers.IntegerField(read_only=True)
    cant = serializers.IntegerField(read_only=True)


class VentasSerialezerWithProductList(VentasSerializerDetail):
    products = DictValidate(many=True)
