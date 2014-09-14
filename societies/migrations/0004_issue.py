# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('societies', '0003_auto_20140911_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('issue_type', models.CharField(choices=[('link', 'Broken Link'), ('name', 'Incorrect Name'), ('region', 'Incorrect Region'), ('custom', 'Custom')], max_length=12, default='custom')),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('society', models.ForeignKey(to='societies.GuitarSociety', on_delete='CASCADE')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
