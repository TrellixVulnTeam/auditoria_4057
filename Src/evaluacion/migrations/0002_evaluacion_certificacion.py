# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 18:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificacion', '0002_auto_20160920_1006'),
        ('evaluacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion',
            name='certificacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='certificacion.Certifiacion'),
            preserve_default=False,
        ),
    ]