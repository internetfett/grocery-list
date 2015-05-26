# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('category', models.ForeignKey(verbose_name=b'Category', to='recipes.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('user', models.ForeignKey(verbose_name=b'User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
                ('unit', models.CharField(max_length=4, choices=[(b'TSP', b'tsp'), (b'TBSP', b'tbsp'), (b'CUP', b'cup'), (b'OZ', b'oz'), (b'LB', b'lb')])),
                ('ingredient', models.ForeignKey(verbose_name=b'Ingredient', to='recipes.Ingredient')),
                ('recipe', models.ForeignKey(verbose_name=b'Recipe', to='recipes.Recipe')),
            ],
        ),
    ]
