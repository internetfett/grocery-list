# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(max_length=4, choices=[(b'UNIT', b'unit'), (b'TSP', b'tsp'), (b'TBSP', b'tbsp'), (b'CUP', b'cup'), (b'OZ', b'oz'), (b'LB', b'lb')]),
        ),
    ]
