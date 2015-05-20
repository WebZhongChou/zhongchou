# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonghu', '0004_remove_chanpin_chanpintableid'),
    ]

    operations = [
        migrations.AddField(
            model_name='chanpin',
            name='hasSale',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chanpin',
            name='Price',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chanpin',
            name='TaocanPrice_1',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chanpin',
            name='TaocanPrice_2',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chanpin',
            name='TaocanPrice_3',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
