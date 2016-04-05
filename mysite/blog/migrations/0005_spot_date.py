# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='spot',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 6, 22, 24, 893382, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
