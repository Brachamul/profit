# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0010_auto_20150201_2229'),
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='is_production',
            field=models.ForeignKey(null=True, blank=True, to='assets.Production'),
            preserve_default=True,
        ),
    ]
