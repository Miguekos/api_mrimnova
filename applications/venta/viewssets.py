from rest_framework import viewsets, status
from django.utils import timezone, dateformat
from rest_framework import serializers
from rest_framework.response import Response
from .models import VentasModelo, ProductModel, ClientModel
from rest_framework.viewsets import GenericViewSet

from .serializer import VentasSerializer, VentasSerializerPost


class VentasViewsetNew(GenericViewSet):
    authentication_classes = ()
    permission_classes = ()
    # serializer_class = VentasSerializerPost
    serializer_class = VentasSerializer
    queryset = VentasModelo.objects.all()

    def create(self, request, *args, **kwargs):
        # print("request.data", request.data)
        try:
            serializer = VentasSerializerPost(data=request.data)
            serializer.is_valid(raise_exception=True)
            # print("asd->", request.data['products'])
            type_sale_validation = request.data['type_sales']

            if type_sale_validation == 0:
                venta = VentasModelo.objects.create(
                    client=ClientModel.objects.get(id=request.data['client']),
                    type_sales=type_sale_validation,
                    address=request.data['address'],
                    details=request.data['details'],
                    descriptions=request.data['descriptions'],
                    materials=request.data['materials'],
                    cost=request.data['cost'],
                    quote=request.data['quote']
                    # products=add_produc,
                    # services=[]
                )
                # VentasModelo.objects.create(venta)
                # serializer.save()
                venta.save()
                # serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            # if type_sale_validation == 1:
            sum_cost = 0
            add_produc = []
            for productos in request.data['products']:
                productos_find = ProductModel.objects.get(id=productos)
                # print("productos_find", productos_find)
                sum_cost = productos_find.cost + sum_cost
                # print("cost", productos_find.cost)
                add_produc.append(productos_find)

            # print("sum_cost", sum_cost)
            # print("add_produc", add_produc)
            venta = VentasModelo.objects.create(
                type_sales=request.data['type_sales'],
                address=request.data['address'],
                type_method_products=request.data['type_method_products'],
                down_payment_producto_cre=request.data['down_payment_producto_cre'],
                quotas_producto_cre=request.data['quotas_producto_cre'],
                type_method_services=request.data['type_method_services'],
                down_payment_servicios_cre=request.data['down_payment_servicios_cre'],
                quotas_servicios_cre=request.data['quotas_servicios_cre'],
                bills_receivable=request.data['bills_receivable'],
                payment_notifications=request.data['payment_notifications'],
                details=request.data['details'],
                descriptions=request.data['descriptions'],
                materials=request.data['materials'],
                cost=sum_cost,
                quote=request.data['quote'],
                client=ClientModel.objects.get(id=request.data['client']),
                # products=add_produc,
                # services=[]
            )
            # VentasModelo.objects.create(venta)
            # serializer.save()
            venta.products.set(add_produc)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except (Exception, NameError) as e:
            return Response("{}".format(e), status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
        # return self.get_paginated_response(self.paginate_queryset(serializer.data))

    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def destroy(self, request):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
