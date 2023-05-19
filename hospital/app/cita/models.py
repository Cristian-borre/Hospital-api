from django.db import models
from app.paciente.models import PacienteModel
from app.medico.models import MedicoModel
from app.consultorio.models import ConsultorioModel

# Create your models here.
CITA_CHOISE = (
    (1,'Pendiente'),
    (2,'Atentido'),
    (3,'Cancelada')
)

class CitaModel(models.Model):

    id = models.AutoField(primary_key=True)
    numero = models.BigIntegerField(db_column='numero')
    fecha = models.DateField(db_column='fecha')
    hora = models.TimeField(db_column='hora')
    paciente = models.ForeignKey(PacienteModel, db_column='paciente', on_delete=models.PROTECT)
    medico = models.ForeignKey(MedicoModel, db_column='medico', on_delete=models.PROTECT)
    consultorio = models.ForeignKey(ConsultorioModel, db_column='consultorio', on_delete=models.PROTECT)
    estado_cita = models.IntegerField(choices=CITA_CHOISE, db_column='estado_cita',default=1)
    observacion = models.CharField(db_column='observacion', max_length=200)
    estado = models.BooleanField(db_column='estado', default=True)
    fecha_creacion = models.DateTimeField(db_column='fecha_creacion', auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cita'
        verbose_name = 'cita'
        verbose_name_plural = 'citas'