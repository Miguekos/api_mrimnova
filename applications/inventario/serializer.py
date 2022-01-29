from rest_framework import serializers
from .models import ProductModel


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
