# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0010_auto_20150201_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='production',
            name='recurrent',
        ),
        migrations.AddField(
            model_name='production',
            name='can_be_recurrent',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
