# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assets', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('amount', models.PositiveSmallIntegerField()),
                ('datetime_placed', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('cash', models.PositiveIntegerField(default=10000)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('left', models.DateTimeField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoredItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('item', models.ForeignKey(to='assets.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('founded', models.DateTimeField(auto_now_add=True)),
                ('map_layout', models.ForeignKey(to='maps.MapLayout')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TownSlot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('on_sale', models.DateTimeField(blank=True, null=True, default=None)),
                ('feature', models.ForeignKey(to='assets.Feature')),
                ('owner', models.ForeignKey(blank=True, null=True, default=None, to='towns.Player')),
                ('slot', models.ForeignKey(to='maps.Slot')),
                ('stored_items', models.ManyToManyField(through='towns.StoredItems', to='assets.Item')),
                ('town', models.ForeignKey(to='towns.Town')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='storeditems',
            name='town_slot',
            field=models.ForeignKey(to='towns.TownSlot'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='town',
            field=models.ForeignKey(to='towns.Town'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bid',
            name='player',
            field=models.ForeignKey(to='towns.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bid',
            name='town_slot',
            field=models.ForeignKey(to='towns.TownSlot'),
            preserve_default=True,
        ),
    ]
