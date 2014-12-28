# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20141018_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='base_illustration',
            field=models.ForeignKey(default=1, to='assets.Illustration'),
        ),
    ]
