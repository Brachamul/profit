# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20141012_1113'),
        ('towns', '0002_auto_20141006_0423'),
    ]

    operations = [
        migrations.AddField(
            model_name='townslot',
            name='illustration',
            field=models.ForeignKey(null=True, to='assets.Illustration'),
            preserve_default=True,
        ),
    ]
