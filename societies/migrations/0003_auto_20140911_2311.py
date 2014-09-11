# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('societies', '0002_auto_20140911_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitarsociety',
            name='region',
            field=models.CharField(blank=True, null=True, max_length=512, default=None),
        ),
    ]
