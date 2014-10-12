# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import assets.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DevelopmentProject',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DevelopmentProjectRequiredMaterial',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('quantity', models.PositiveSmallIntegerField(validators=[assets.models.validate_material_quantity], blank=True, default=0)),
                ('development_project', models.ForeignKey(to='assets.DevelopmentProject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('min_price', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Illustration',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('image', models.ImageField(upload_to='/illustrations/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('description', models.TextField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Upgrade',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('feature', models.ForeignKey(to='assets.Feature')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UpgradeRequiredMaterial',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('quantity', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('item', models.ForeignKey(to='assets.Item')),
                ('upgrade', models.ForeignKey(to='assets.Upgrade')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='upgrade',
            name='required_materials',
            field=models.ManyToManyField(to='assets.Item', through='assets.UpgradeRequiredMaterial'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feature',
            name='illustration',
            field=models.ManyToManyField(to='assets.Illustration'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='developmentprojectrequiredmaterial',
            name='item',
            field=models.ForeignKey(to='assets.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='developmentproject',
            name='becomes',
            field=models.ForeignKey(to='assets.Feature', related_name='Project Result'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='developmentproject',
            name='required_materials',
            field=models.ManyToManyField(to='assets.Item', through='assets.DevelopmentProjectRequiredMaterial'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='developmentproject',
            name='was',
            field=models.ForeignKey(to='assets.Feature', related_name='Project Source'),
            preserve_default=True,
        ),
    ]
