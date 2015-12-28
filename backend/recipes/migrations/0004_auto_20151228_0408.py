# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0003_auto_20151217_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(default=1, verbose_name=b'User', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='user',
            field=models.ForeignKey(default=1, verbose_name=b'User', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
