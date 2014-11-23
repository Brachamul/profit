# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_developmentproject_required_amount_of_workers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='base_illustration',
            field=models.ForeignKey(to='assets.Illustration'),
        ),
    ]
