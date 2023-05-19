from rest_framework import serializers
from .models import CitaModel
from app.paciente.models import PacienteModel
from app.paciente.serializer import PacienteSerializer
from app.medico.models import MedicoModel
from app.medico.serializer import MedicoSerializer
from app.consultorio.models import ConsultorioModel
from app.consultorio.serializer import ConsultorioSerializer

class CitaSerializer(serializers.HyperlinkedModelSerializer):
    paciente_id = serializers.PrimaryKeyRelatedField(queryset=PacienteModel.objects.all())
    paciente = PacienteSerializer(read_only=True)
    medico_id = serializers.PrimaryKeyRelatedField(queryset=MedicoModel.objects.all())
    medico = MedicoSerializer(read_only=True)
    consultorio_id = serializers.PrimaryKeyRelatedField(queryset=ConsultorioModel.objects.all())
    consultorio = ConsultorioSerializer(read_only=True)
    class Meta:
        model = CitaModel
        fields = ['id','numero','fecha','hora','paciente','paciente_id','medico','medico_id','consultorio','consultorio_id','estado_cita','observacion']