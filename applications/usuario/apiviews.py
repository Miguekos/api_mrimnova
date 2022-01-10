# importar el UserSerializer
from rest_framework import generics
from .serializer import UserSerializer

class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer