# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonghu', '0002_remove_users_chanpinkutableid'),
    ]

    operations = [
        migrations.AddField(
            model_name='chanpin',
            name='Taocanjianjie_1',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chanpin',
            name='Taocanjianjie_2',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chanpin',
            name='Taocanjianjie_3',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
