# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_run_is_production'),
    ]

    operations = [
        migrations.RenameField(
            model_name='run',
            old_name='recurrent',
            new_name='is_recurrent',
        ),
        migrations.RemoveField(
            model_name='run',
            name='pay',
        ),
        migrations.AlterField(
            model_name='run',
            name='remaining_cycles',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
