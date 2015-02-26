# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150224_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='login_required',
            new_name='is_sytem',
        ),
        migrations.RemoveField(
            model_name='page',
            name='is_system',
        ),
    ]
