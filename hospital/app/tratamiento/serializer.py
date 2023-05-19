from rest_framework import serializers
from .models import TratamientoModel
from app.paciente.models import PacienteModel
from app.paciente.serializer import PacienteSerializer
from app.medicamento.models import MedicamentoModel
from app.medicamento.serializer import MedicamentoSerializer

class TratamientoSerializer(serializers.HyperlinkedModelSerializer):
    paciente_id = serializers.PrimaryKeyRelatedField(queryset=PacienteModel.objects.all())
    paciente = PacienteSerializer(read_only=True)
    medicamento_id = serializers.PrimaryKeyRelatedField(queryset=MedicamentoModel.objects.all())
    medicamento = MedicamentoSerializer(read_only=True)
    class Meta:
        model = TratamientoModel
        fields = ['id','numero','paciente','paciente_id','fecha_asignada','medicamento','medicamento_id','fecha_inicio','fecha_fin','observaciones']