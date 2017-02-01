# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0002_teleconsultor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('texto', models.CharField(max_length=1000)),
                ('data', models.DateField()),
                ('solicitante', models.ForeignKey(to='desafio.Solicitante')),
                ('teleconsultor', models.ForeignKey(to='desafio.Teleconsultor')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='solicitacao',
            unique_together=set([('solicitante', 'data')]),
        ),
    ]
