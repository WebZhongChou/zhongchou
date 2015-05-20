# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chanpin',
            fields=[
                ('ChanPinID', models.AutoField(serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=15)),
                ('picture', models.CharField(max_length=50)),
                ('jieshao', models.TextField()),
                ('TaocanName_1', models.CharField(max_length=15)),
                ('TaocanPrice_1', models.IntegerField()),
                ('TaocanName_2', models.CharField(max_length=15)),
                ('TaocanPrice_2', models.IntegerField()),
                ('TaocanName_3', models.CharField(max_length=15)),
                ('TaocanPrice_3', models.IntegerField()),
                ('Price', models.IntegerField()),
                ('CreateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('DueTime', models.DateTimeField()),
                ('ChanPinTableID', models.BigIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('UserID', models.AutoField(serialize=False, primary_key=True)),
                ('Username', models.CharField(max_length=15)),
                ('Password', models.CharField(max_length=15)),
                ('TouXiang', models.CharField(max_length=50)),
                ('ChanPinKuTableID', models.BigIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
