# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0002_evaluacion_certificacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calificacion',
            name='active',
        ),
        migrations.AddField(
            model_name='calificacion',
            name='comentario',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='cumplimiento',
            field=models.BooleanField(default=False),
        ),
    ]