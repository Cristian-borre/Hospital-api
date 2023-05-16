from django.db import models

# Create your models here.

class ConsultorioModel(models.Model):

    id = models.AutoField(primary_key=True)
    numero = models.BigIntegerField(db_column='numero')
    nombre = models.CharField(db_column='nombre', max_length=50)
    estado = models.BooleanField(db_column='estado', default=True)
    fecha = models.DateTimeField(db_column='fecha', auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'consultorio'
        verbose_name = 'consultorio'
        verbose_name_plural = 'consultorios'