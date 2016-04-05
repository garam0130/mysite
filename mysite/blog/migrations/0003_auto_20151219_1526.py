# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151219_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='spot',
            name='lng',
        ),
        migrations.AddField(
            model_name='spot',
            name='lnglat',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
    ]
