# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-11-28 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_symbology', '0005_auto_20171023_0631'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorRamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('definition', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='style',
            name='type',
            field=models.CharField(choices=[('US', 'S\xedmbolo \xfanico'), ('UV', 'Valores \xfanicos'), ('IN', 'Intervalos'), ('EX', 'Expresiones'), ('CP', 'Agrupaci\xf3n de puntos'), ('CT', 'Tabla de color'), ('CH', 'Gr\xe1ficas')], default='US', max_length=2),
        ),
    ]
