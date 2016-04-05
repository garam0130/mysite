# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
                ('URL', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('map_marker', models.IntegerField()),
            ],
        ),
    ]
