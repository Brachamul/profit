# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0009_auto_20150201_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionRequiredMaterial',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('quantity', models.PositiveSmallIntegerField(default=0, blank=True)),
                ('item', models.ForeignKey(to='assets.Item')),
                ('production', models.ForeignKey(to='assets.Production')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='production',
            name='recurrent',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
