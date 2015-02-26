# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20150224_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='is_system',
            new_name='login_required',
        ),
    ]
