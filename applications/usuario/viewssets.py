from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializer import UserSerializer, UsuarioSerializer

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User


class UserCreate(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LoginViewset(viewsets.ViewSet):
    permission_classes = ()

    def create(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token = Token.objects.get_or_create(user=user)
            return Response({
                "token": "{}".format(token[0]),
                "created" : "{}".format(token[1]),
            })
            # Redirect to a success page.
        else:
            return Response(
                {
                    "error": "Credenciales incorrectas"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        """
        user = authenticate(username=username, password=password)
        print("user", user)
        if user is not None:
            return Response({"token": "{}".format(user)})
        else:
            return Response(
                {
                    "error": "Credenciales incorrectas"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        """
