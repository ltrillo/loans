# Generated by Django 2.1.2 on 2018-10-08 00:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condiciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ComisionFlat', models.DecimalField(decimal_places=3, max_digits=5)),
                ('PorcentajePrestamo', models.DecimalField(decimal_places=3, max_digits=5)),
                ('InteresAnual', models.DecimalField(decimal_places=3, max_digits=5)),
                ('PenalidadMora', models.DecimalField(decimal_places=3, max_digits=5)),
                ('Plazo', models.DecimalField(decimal_places=0, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=8, max_digits=15)),
                ('Plazo', models.DecimalField(decimal_places=0, max_digits=2)),
                ('FechaPrestamo', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Apellido', models.CharField(max_length=35)),
                ('Nombre', models.CharField(max_length=35)),
                ('DNI', models.CharField(max_length=8)),
                ('Sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1)),
            ],
        ),
    ]