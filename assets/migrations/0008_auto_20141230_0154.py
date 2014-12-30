# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_auto_20141230_0122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='production',
            old_name='features',
            new_name='feature',
        ),
    ]
