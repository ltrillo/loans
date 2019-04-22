# Generated by Django 2.1.2 on 2018-10-19 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora', '0009_prestamo_us'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prestamo_us',
            old_name='Usuario_us',
            new_name='User',
        ),
        migrations.AlterField(
            model_name='prestamo_us',
            name='Cuotas_Impago_us',
            field=models.DecimalField(decimal_places=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='prestamo_us',
            name='Fecha_us',
            field=models.DateTimeField(),
        ),
    ]