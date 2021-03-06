# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0005_auto_20170902_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='abstract',
            field=models.TextField(blank=True, help_text='A concise summary of your talk in one or two sentences. You can use markdown here.', null=True, verbose_name='Abstract'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='description',
            field=models.TextField(blank=True, help_text='A full-text description of your talk and its contents. You can use markdown here.', null=True, verbose_name='Description'),
        ),
    ]
