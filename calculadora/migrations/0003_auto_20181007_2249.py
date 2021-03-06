# Generated by Django 2.1.2 on 2018-10-08 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora', '0002_auto_20181007_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='condiciones',
            name='PlazoMeses',
        ),
        migrations.RemoveField(
            model_name='prestamo',
            name='Plazo',
        ),
        migrations.AddField(
            model_name='prestamo',
            name='PlazoMeses',
            field=models.CharField(choices=[('6', '6 Meses'), ('12', '12 Meses'), ('18', '18 Meses'), ('24', '24 Meses')], default='6', max_length=2),
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='ComisionFlat',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='InteresAnual',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='PenalidadMora',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='PorcentajePrestamo',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
