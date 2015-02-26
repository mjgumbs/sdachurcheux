# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_is_system'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='is_system',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
