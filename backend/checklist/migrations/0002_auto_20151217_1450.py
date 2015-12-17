# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20151217_1450'),
        ('checklist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistitem',
            name='category',
            field=models.ForeignKey(verbose_name=b'Category', blank=True, to='recipes.Category', null=True),
        ),
        migrations.AlterField(
            model_name='checklistingredient',
            name='unit',
            field=models.CharField(max_length=4, choices=[(b'unit', b'unit'), (b'tsp', b'tsp'), (b'tbsp', b'tbsp'), (b'cup', b'cup'), (b'oz', b'oz'), (b'lb', b'lb')]),
        ),
        migrations.AlterField(
            model_name='checklistitem',
            name='unit',
            field=models.CharField(max_length=4, choices=[(b'unit', b'unit'), (b'tsp', b'tsp'), (b'tbsp', b'tbsp'), (b'cup', b'cup'), (b'oz', b'oz'), (b'lb', b'lb')]),
        ),
    ]
