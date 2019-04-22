# Generated by Django 2.1.2 on 2018-10-23 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora', '0022_auto_20181023_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prestamo',
            old_name='monto_ONX_Prestamo',
            new_name='Monto',
        ),
        migrations.AddField(
            model_name='prestamo',
            name='Couota_Interes',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=17),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='Cuota_Capital',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=17),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='Cuota_Mensual',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=17),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='Cuotas_Garantia',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=17),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='Garantia',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=17),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='Penalidad',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prestamo',
            name='Transferido',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]