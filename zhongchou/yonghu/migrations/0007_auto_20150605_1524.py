# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonghu', '0006_auto_20150603_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buychanpin',
            old_name='ChanPinID',
            new_name='ChanpinID',
        ),
    ]
