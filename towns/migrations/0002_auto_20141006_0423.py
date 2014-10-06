# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('towns', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='town',
            name='ended',
            field=models.DateTimeField(null=True, default=None, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='town',
            name='phase',
            field=models.PositiveSmallIntegerField(null=True, default=0),
            preserve_default=True,
        ),
    ]
