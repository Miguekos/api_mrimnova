from rest_framework import viewsets
from django.utils import timezone, dateformat
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet
from .models import ProductModel, FacturaModel

from .serializer import ProductoSerializer, ProductoSerializerNew


# class ProductViewset(viewsets.ModelViewSet):
#     serializer_class = ProductoSerializer
#     queryset = ProductModel.objects.all()

class ProductViewset(GenericViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = ProductoSerializer
    queryset = ProductModel.objects.all()

    def create(self, request, *args, **kwargs):
        # print("request.data", request.data)
        try:
            serializer = ProductoSerializerNew(data=request.data)
            serializer.is_valid(raise_exception=True)
            # serializer = ProductoSerializer(data=request.data)
            # _json = {
            #     'client': request.data['client'],
            #     'type_sales': request.data['type_sales'],
            #     'address': request.data['address'],
            #     "details": request.data['details'],
            #     "descriptions": request.data['descriptions'],
            #     "materials": request.data['materials'],
            #     "cost": request.data['cost'],
            #     "quote": request.data['quote']
            # }
            # serializer = ProductoSerializer(data=_json)

            # seriales = request.data['serial_number']
            # seriales_count = len(seriales)
            # print("serial_number", request.data['serial_number'])

            products_ready = []
            factura = FacturaModel.objects.get(id=1)

            for produc in serializer.validated_data['serial_number']:
                # print("asd", produc)
                pruductos_por_seriales = ProductModel(
                    name="{} - {}".format(serializer.validated_data['name'], produc),
                    marca=serializer.validated_data['marca'],
                    modelo=serializer.validated_data['modelo'],
                    code=serializer.validated_data['code'],
                    internal_product_code=serializer.validated_data['internal_product_code'],
                    bar_code=serializer.validated_data['bar_code'],
                    quantity=serializer.validated_data['quantity'],
                    serial_number=produc,
                    obervations=serializer.validated_data['obervations'],
                    tickets_purchases=serializer.validated_data['tickets_purchases'],
                    purchase_cost=serializer.validated_data['purchase_cost'],
                    outflows_sales=serializer.validated_data['outflows_sales'],
                    cost=serializer.validated_data['cost'],
                    description=serializer.validated_data['description'],
                    date_received=timezone.now(),
                    date_of_entry=timezone.now(),
                    invoice_relation=factura
                )
                # print("pruductos_por_seriales", pruductos_por_seriales)
                products_ready.append(pruductos_por_seriales)

            # serializer.save()
            ProductModel.objects.bulk_create(products_ready)
            # headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return Response("serializer.data")
        except (Exception, NameError) as e:
            return Response("{}".format(e), status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
        # return self.get_paginated_response(self.paginate_queryset(serializer.data))

    def update(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def destroy(self, request, pk):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
