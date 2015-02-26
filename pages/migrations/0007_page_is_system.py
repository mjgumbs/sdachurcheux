# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20150224_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='is_system',
            field=models.BooleanField(default=False, db_index=True),
            preserve_default=True,
        ),
    ]
