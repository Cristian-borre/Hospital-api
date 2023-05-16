from django.db import models

# Create your models here.

class MedicoModel(models.Model):

    id = models.AutoField(primary_key=True)
    documento = models.BigIntegerField(db_column='documento')
    nombre = models.CharField(db_column='nombre', max_length=50)
    apellido = models.CharField(db_column='apellido', max_length=50)
    telefono = models.BigIntegerField(db_column='telefono')
    estado = models.BooleanField(db_column='estado', default=True)
    fecha = models.DateTimeField(db_column='fecha', auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'medico'
        verbose_name = 'medico'
        verbose_name_plural = 'medicos'