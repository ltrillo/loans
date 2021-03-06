# Generated by Django 2.1.2 on 2018-10-09 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora', '0003_auto_20181007_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plazos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Plazo')),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='PlazoMeses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='calculadora.Plazos'),
        ),
    ]
