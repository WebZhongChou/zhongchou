# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonghu', '0005_auto_20150520_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='buyChanpin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('UserID', models.IntegerField(max_length=15)),
                ('ChanPinID', models.IntegerField(max_length=15)),
                ('ChanpinName', models.CharField(max_length=15)),
                ('price', models.IntegerField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='pinglun',
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
        migrations.RemoveField(
            model_name='users',
            name='TouXiang',
        ),
        migrations.AddField(
            model_name='chanpin',
            name='UserID',
            field=models.IntegerField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
