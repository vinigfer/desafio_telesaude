# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0003_auto_20170201_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitante',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='teleconsultor',
            name='crm',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='teleconsultor',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
