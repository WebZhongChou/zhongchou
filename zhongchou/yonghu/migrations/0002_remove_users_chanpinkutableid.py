# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonghu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='ChanPinKuTableID',
        ),
    ]
