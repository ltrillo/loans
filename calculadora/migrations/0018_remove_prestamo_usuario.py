# Generated by Django 2.1.2 on 2018-10-23 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora', '0017_auto_20181023_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestamo',
            name='Usuario',
        ),
    ]