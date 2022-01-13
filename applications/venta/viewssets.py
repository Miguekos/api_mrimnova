from rest_framework import viewsets, status
from django.utils import timezone, dateformat
from rest_framework import serializers
from rest_framework.response import Response
from .models import VentasModelo
from rest_framework.viewsets import GenericViewSet

from .serializer import VentasSerializer, VentasSerializerPost


class VentasViewsetNew(GenericViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = VentasSerializer
    queryset = VentasModelo.objects.all()

    def create(self, request, *args, **kwargs):
        print("request.data", request.data)
        try:
            _json = {
                'client': request.data['client'],
                'type_sales': request.data['type_sales'],
                'address': request.data['address'],
                "details": request.data['details'],
                "descriptions": request.data['descriptions'],
                "materials": request.data['materials'],
                "cost": request.data['cost'],
                "quote": request.data['quote']
            }
            serializer = VentasSerializerPost(data=_json)
            serializer.is_valid(raise_exception=True)
            serializer.save()
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
