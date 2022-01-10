from rest_framework import viewsets
from django.utils import timezone, dateformat
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import ProductModel

from .serializer import ProductoSerializer


class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = ProductModel.objects.all()
