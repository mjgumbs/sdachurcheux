# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20150224_1258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='is_sytem',
            new_name='is_system',
        ),
    ]
