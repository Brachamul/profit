# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20141011_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='developmentproject',
            name='illustration',
            field=models.ForeignKey(to='assets.Illustration', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='upgrade',
            name='illustration',
            field=models.ForeignKey(to='assets.Illustration', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='illustration',
            name='image',
            field=models.ImageField(upload_to='illustrations'),
        ),
    ]
