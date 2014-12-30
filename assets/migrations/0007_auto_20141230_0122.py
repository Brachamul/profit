# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_auto_20141227_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(max_length=1000, blank=True)),
                ('workers', models.PositiveSmallIntegerField(null=True, default=0, blank=True)),
                ('features', models.ManyToManyField(to='assets.Feature')),
                ('illustration', models.ForeignKey(null=True, to='assets.Illustration')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductionOutput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
            name='output',
            field=models.ManyToManyField(to='assets.Item', through='assets.ProductionOutput'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='developmentprojectrequiredmaterial',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='feature',
            name='description',
            field=models.TextField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='upgrade',
            name='description',
            field=models.TextField(max_length=1000, blank=True),
        ),
    ]
