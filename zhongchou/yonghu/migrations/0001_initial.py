# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='buyChanpin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('UserID', models.IntegerField(max_length=15)),
                ('ChanpinID', models.IntegerField(max_length=15)),
                ('ChanpinName', models.CharField(max_length=15)),
                ('price', models.IntegerField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Chanpin',
            fields=[
                ('ChanPinID', models.AutoField(serialize=False, primary_key=True)),
                ('UserID', models.IntegerField(max_length=15)),
                ('Name', models.CharField(max_length=15)),
                ('picture', models.CharField(max_length=50)),
                ('jieshao', models.TextField()),
                ('TaocanName_1', models.CharField(max_length=15)),
                ('TaocanPrice_1', models.FloatField()),
                ('Taocanjianjie_1', models.TextField(null=True)),
                ('TaocanName_2', models.CharField(max_length=15)),
                ('TaocanPrice_2', models.FloatField()),
                ('Taocanjianjie_2', models.TextField(null=True)),
                ('TaocanName_3', models.CharField(max_length=15)),
                ('TaocanPrice_3', models.FloatField()),
                ('Taocanjianjie_3', models.TextField(null=True)),
                ('Price', models.FloatField()),
                ('hasSale', models.FloatField()),
                ('CreateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('DueTime', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pinglun',
            fields=[
                ('PingLunID', models.AutoField(serialize=False, primary_key=True)),
                ('UserID', models.IntegerField(max_length=15)),
                ('ChanPinID', models.IntegerField(max_length=15)),
                ('Content', models.TextField(null=True)),
                ('Time', models.DateTimeField()),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
