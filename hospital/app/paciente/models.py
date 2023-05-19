from django.db import models

# Create your models here.
SEXO_CHOISE= (
        (1, 'Masculino'),
        (2, 'Femenino'),
)

class PacienteModel(models.Model):

    id = models.AutoField(primary_key=True)
    documento = models.BigIntegerField(db_column='documento')
    nombre = models.CharField(db_column='nombre', max_length=50)
    apellido = models.CharField(db_column='apellido', max_length=50)
    telefono = models.BigIntegerField(db_column='telefono')
    fecha_nacimiento = models.DateField(db_column='fecha_nacimiento')
    sexo = models.IntegerField(choices=SEXO_CHOISE, db_column='sexo')
    estado = models.BooleanField(db_column='estado', default=True)
    fecha = models.DateTimeField(db_column='fecha', auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'paciente'
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'