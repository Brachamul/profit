# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_auto_20141227_2203'),
        ('towns', '0004_auto_20141018_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerStuff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField(default=0, blank=True)),
                ('item', models.ForeignKey(to='assets.Item')),
                ('player', models.ForeignKey(to='towns.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='player',
            name='stuff',
            field=models.ManyToManyField(through='towns.PlayerStuff', to='assets.Item'),
            preserve_default=True,
        ),
    ]
