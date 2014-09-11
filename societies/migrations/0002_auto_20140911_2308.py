# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('societies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitarsociety',
            name='region',
            field=models.CharField(default=None, max_length=512, null=True),
        ),
    ]
