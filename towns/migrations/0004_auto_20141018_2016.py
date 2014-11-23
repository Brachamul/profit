# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('towns', '0003_townslot_illustration'),
    ]

    operations = [
        migrations.AddField(
            model_name='town',
            name='floating_wealth',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='town',
            name='minimum_wage',
            field=models.PositiveSmallIntegerField(default=100),
            preserve_default=True,
        ),
    ]
