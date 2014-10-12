# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='illustration',
        ),
        migrations.AddField(
            model_name='feature',
            name='base_illustration',
            field=models.ForeignKey(null=True, to='assets.Illustration', blank=True),
            preserve_default=True,
        ),
    ]
