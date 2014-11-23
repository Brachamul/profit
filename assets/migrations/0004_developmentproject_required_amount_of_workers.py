# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20141012_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='developmentproject',
            name='required_amount_of_workers',
            field=models.PositiveSmallIntegerField(default=4),
            preserve_default=True,
        ),
    ]
