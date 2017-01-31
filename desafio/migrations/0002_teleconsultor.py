# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teleconsultor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(max_length=50)),
                ('crm', models.IntegerField(unique=True)),
                ('data_formatura', models.DateField()),
            ],
        ),
    ]
