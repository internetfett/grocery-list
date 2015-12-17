# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20150526_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='category',
            field=models.ForeignKey(verbose_name=b'Category', blank=True, to='recipes.Category', null=True),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='recipe',
            field=models.ForeignKey(related_name='items', verbose_name=b'Recipe', to='recipes.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(max_length=4, choices=[(b'unit', b'unit'), (b'tsp', b'tsp'), (b'tbsp', b'tbsp'), (b'cup', b'cup'), (b'oz', b'oz'), (b'lb', b'lb')]),
        ),
    ]
