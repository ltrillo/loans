# Generated by Django 2.1.2 on 2018-10-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora', '0020_auto_20181023_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='monto',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=17),
        ),
    ]