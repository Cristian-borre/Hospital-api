from django.db import models

# Create your models here.

class MedicamentoModel(models.Model):

    id = models.AutoField(primary_key=True)
    numero = models.BigIntegerField(db_column='numero')
    nombre = models.CharField(db_column='nombre', max_length=50)
    descripcion = models.CharField(db_column='descripcion', max_length=100)
    estado = models.BooleanField(db_column='estado', default=True)
    fecha = models.DateTimeField(db_column='fecha', auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'medicamento'
        verbose_name = 'medicamento'
        verbose_name_plural = 'medicamentos'