# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_spot_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='date',
            field=models.DateField(),
        ),
    ]
