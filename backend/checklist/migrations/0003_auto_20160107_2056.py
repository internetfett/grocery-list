# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0002_auto_20151217_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistingredient',
            name='amount',
            field=models.DecimalField(default=1, max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='checklistitem',
            name='amount',
            field=models.DecimalField(default=1, max_digits=6, decimal_places=3),
        ),
    ]
