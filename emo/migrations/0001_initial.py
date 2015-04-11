# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('abbr', models.CharField(max_length=3)),
                ('angry_avg', models.FloatField(default=0.0, blank=True)),
                ('sad_avg', models.FloatField(default=0.0, blank=True)),
                ('neutral_avg', models.FloatField(default=0.0, blank=True)),
                ('surprise_avg', models.FloatField(default=0.0, blank=True)),
                ('fear_avg', models.FloatField(default=0.0, blank=True)),
                ('happy_avg', models.FloatField(default=0.0, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_scanned', models.IntegerField(default=0)),
                ('angry_new', models.FloatField(default=0.0)),
                ('sad_new', models.FloatField(default=0.0)),
                ('neutral_new', models.FloatField(default=0.0)),
                ('surprise_new', models.FloatField(default=0.0)),
                ('fear_new', models.FloatField(default=0.0)),
                ('happy_new', models.FloatField(default=0.0)),
                ('angry_avg', models.FloatField(default=0.0, blank=True)),
                ('sad_avg', models.FloatField(default=0.0, blank=True)),
                ('neutral_avg', models.FloatField(default=0.0, blank=True)),
                ('surprise_avg', models.FloatField(default=0.0, blank=True)),
                ('fear_avg', models.FloatField(default=0.0, blank=True)),
                ('happy_avg', models.FloatField(default=0.0, blank=True)),
                ('department', models.ForeignKey(to='emo.Department')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
