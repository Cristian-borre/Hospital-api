from rest_framework import serializers
from .models import PacienteModel

class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PacienteModel
        fields = ['id','documento','nombre','apellido','telefono','fecha_nacimiento','sexo']