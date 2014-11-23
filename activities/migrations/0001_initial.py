# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20141012_1113'),
        ('towns', '0003_townslot_illustration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('date_completed', models.DateTimeField(null=True, blank=True)),
                ('pay', models.PositiveSmallIntegerField()),
                ('recurrent', models.BooleanField(default=False)),
                ('remaining_cycles', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('is_development', models.ForeignKey(to='assets.DevelopmentProject', null=True, blank=True)),
                ('is_upgrade', models.ForeignKey(to='assets.Upgrade', null=True, blank=True)),
                ('town_slot', models.ForeignKey(to='towns.TownSlot')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
