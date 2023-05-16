from rest_framework import serializers
from .models import ConsultorioModel

class ConsultorioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConsultorioModel
        fields = ['id','numero','nombre','estado']