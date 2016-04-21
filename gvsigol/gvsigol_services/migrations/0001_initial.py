# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gvsigol_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=500)),
                ('roles', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Datastore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('connection_params', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=150)),
                ('abstract', models.CharField(max_length=5000)),
                ('type', models.CharField(max_length=150)),
                ('metadata_uuid', models.CharField(blank=True, max_length=100, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('queryable', models.BooleanField(default=True)),
                ('cached', models.BooleanField(default=True)),
                ('single_image', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
                ('datastore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gvsigol_services.Datastore')),
            ],
        ),
        migrations.CreateModel(
            name='LayerGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('cached', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LayerReadGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gvsigol_auth.UserGroup')),
                ('layer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gvsigol_services.Layer')),
            ],
        ),
        migrations.CreateModel(
            name='LayerWriteGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gvsigol_auth.UserGroup')),
                ('layer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gvsigol_services.Layer')),
            ],
        ),
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('uri', models.CharField(max_length=500)),
                ('wms_endpoint', models.CharField(blank=True, max_length=500, null=True)),
                ('wfs_endpoint', models.CharField(blank=True, max_length=500, null=True)),
                ('wcs_endpoint', models.CharField(blank=True, max_length=500, null=True)),
                ('cache_endpoint', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='layer',
            name='layer_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gvsigol_services.LayerGroup'),
        ),
        migrations.AddField(
            model_name='datastore',
            name='workspace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gvsigol_services.Workspace'),
        ),
    ]
