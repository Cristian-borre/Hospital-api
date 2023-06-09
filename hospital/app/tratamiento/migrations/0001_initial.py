# Generated by Django 4.2.1 on 2023-05-19 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paciente', '0001_initial'),
        ('medicamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TratamientoModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.BigIntegerField(db_column='numero')),
                ('fecha_asignada', models.DateField(db_column='fecha_asignada')),
                ('fecha_inicio', models.DateField(db_column='fecha_inicio')),
                ('fecha_fin', models.DateField(db_column='fecha_fin')),
                ('observaciones', models.CharField(db_column='observaciones', max_length=200)),
                ('estado', models.BooleanField(db_column='estado', default=True)),
                ('fecha', models.DateTimeField(auto_now_add=True, db_column='fecha')),
                ('medicamento', models.ForeignKey(db_column='medicamento', on_delete=django.db.models.deletion.PROTECT, to='medicamento.medicamentomodel')),
                ('paciente', models.ForeignKey(db_column='paciente', on_delete=django.db.models.deletion.PROTECT, to='paciente.pacientemodel')),
            ],
            options={
                'verbose_name': 'tratamiento',
                'verbose_name_plural': 'tratamientos',
                'db_table': 'tratamiento',
                'managed': True,
            },
        ),
    ]
