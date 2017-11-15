# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-15 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Role', verbose_name='角色'),
        ),
        migrations.AlterField(
            model_name='user',
            name='face',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='电话'),
        ),
    ]
