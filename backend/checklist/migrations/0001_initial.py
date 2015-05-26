# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20150526_2020'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('user', models.ForeignKey(verbose_name=b'User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChecklistIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
                ('amount', models.DecimalField(default=1, max_digits=6, decimal_places=2)),
                ('unit', models.CharField(max_length=4, choices=[(b'UNIT', b'unit'), (b'TSP', b'tsp'), (b'TBSP', b'tbsp'), (b'CUP', b'cup'), (b'OZ', b'oz'), (b'LB', b'lb')])),
                ('checklist', models.ForeignKey(verbose_name=b'Checklist', to='checklist.Checklist')),
                ('ingredient', models.ForeignKey(verbose_name=b'Ingredient', to='recipes.Ingredient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChecklistItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
                ('amount', models.DecimalField(default=1, max_digits=6, decimal_places=2)),
                ('unit', models.CharField(max_length=4, choices=[(b'UNIT', b'unit'), (b'TSP', b'tsp'), (b'TBSP', b'tbsp'), (b'CUP', b'cup'), (b'OZ', b'oz'), (b'LB', b'lb')])),
                ('name', models.CharField(max_length=128)),
                ('checklist', models.ForeignKey(verbose_name=b'Checklist', to='checklist.Checklist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Exclusion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingredient', models.ForeignKey(verbose_name=b'Ingredient', to='recipes.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Repeatable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingredient', models.ForeignKey(verbose_name=b'Ingredient', blank=True, to='checklist.ChecklistIngredient', null=True)),
                ('item', models.ForeignKey(verbose_name=b'Item', blank=True, to='checklist.ChecklistItem', null=True)),
            ],
        ),
    ]
