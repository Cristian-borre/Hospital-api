from rest_framework import serializers
from .models import MedicoModel

class MedicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedicoModel
        fields = ['id','documento','nombre','apellido','telefono','estado']