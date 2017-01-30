# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitante',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('telefone', models.CharField(max_length=11)),
            ],
        ),
    ]
