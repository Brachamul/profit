# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0008_auto_20141230_0154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='production',
            old_name='workers',
            new_name='required_amount_of_workers',
        ),
        migrations.AlterField(
            model_name='developmentproject',
            name='required_amount_of_workers',
            field=models.PositiveSmallIntegerField(null=True, default=0, blank=True),
        ),
    ]
