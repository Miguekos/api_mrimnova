from rest_framework import viewsets, status
from django.utils import timezone, dateformat
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import ClientModel
from rest_framework.viewsets import GenericViewSet

from .serializer import ClientSerializer, ClientSerializerPost

class ClintesViewsetNew(GenericViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = ClientSerializer
    queryset = ClientModel.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = ClientSerializerPost(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

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


class ClintesViewset(viewsets.ViewSet):
    authentication_classes = ()
    permission_classes = ()
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def list(self, request):
        queryset = ClientModel.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ClientSerializerPost(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        # queryset = ClientModel.objects.all()
        # serializer = ClientSerializerPost(queryset)
        # return Response(serializer.data)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
