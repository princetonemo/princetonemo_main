# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emo', '0002_auto_20150411_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='num_students',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
