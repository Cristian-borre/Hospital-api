from rest_framework import serializers
from .models import MedicamentoModel

class MedicamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedicamentoModel
        fields = ['id','numero','nombre','descripcion']