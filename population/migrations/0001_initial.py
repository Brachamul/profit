# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('towns', '0003_townslot_illustration'),
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('number', models.PositiveSmallIntegerField()),
                ('savings', models.PositiveSmallIntegerField()),
                ('job', models.ForeignKey(null=True, to='activities.Run', blank=True)),
                ('town', models.ForeignKey(to='towns.Town')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
