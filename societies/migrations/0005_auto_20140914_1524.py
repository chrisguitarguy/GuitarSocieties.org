# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('societies', '0004_issue'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guitarsociety',
            options={'verbose_name_plural': 'Guitar Societies'},
        ),
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='issue',
            name='created',
            field=models.DateTimeField(default=django.utils.datetime_safe.date.today, auto_now_add=True),
            preserve_default=False,
        ),
    ]
