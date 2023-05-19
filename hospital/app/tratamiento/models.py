from django.db import models
from app.medicamento.models import MedicamentoModel
from app.paciente.models import PacienteModel

# Create your models here.

class TratamientoModel(models.Model):

    id = models.AutoField(primary_key=True)
    numero = models.BigIntegerField(db_column='numero')
    paciente = models.ForeignKey(PacienteModel, db_column='paciente', on_delete=models.PROTECT)
    fecha_asignada = models.DateField(db_column='fecha_asignada')
    medicamento = models.ForeignKey(MedicamentoModel, db_column='medicamento', on_delete=models.PROTECT)
    fecha_inicio = models.DateField(db_column='fecha_inicio')
    fecha_fin = models.DateField(db_column='fecha_fin')
    observaciones = models.CharField(db_column='observaciones', max_length=200)
    estado = models.BooleanField(db_column='estado', default=True)
    fecha = models.DateTimeField(db_column='fecha', auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'tratamiento'
        verbose_name = 'tratamiento'
        verbose_name_plural = 'tratamientos'