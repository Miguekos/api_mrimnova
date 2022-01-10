from rest_framework import serializers
from .models import PersonalModel


class PersonalModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalModel
        fields = '__all__'