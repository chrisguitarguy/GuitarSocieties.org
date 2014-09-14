# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('societies', '0005_auto_20140914_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitarsociety',
            name='active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guitarsociety',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.datetime_safe.datetime.utcnow),
            preserve_default=False,
        ),
    ]
