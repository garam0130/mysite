# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='URL',
        ),
        migrations.RemoveField(
            model_name='spot',
            name='map_marker',
        ),
        migrations.AddField(
            model_name='spot',
            name='lat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='spot',
            name='lng',
            field=models.IntegerField(default=0),
        ),
    ]
