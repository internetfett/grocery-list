# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20160124_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='calories',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
