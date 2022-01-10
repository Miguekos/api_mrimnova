from rest_framework import viewsets
from .models import PersonalModel

from .serializer import PersonalModelSerializer

class PersonalViewset(viewsets.ModelViewSet):
    serializer_class = PersonalModelSerializer
    queryset = PersonalModel.objects.all()
