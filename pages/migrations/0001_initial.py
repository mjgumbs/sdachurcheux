# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import pages.models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('url', models.CharField(help_text="Example: '/about/contact/'. Make sure to have leading and trailing slashes.", validators=[django.core.validators.RegexValidator(regex='^[-\\w/\\.~]+$', message='This value must contain only letters, numbers, dots, underscores, dashes, slashes or tildes.'), pages.models.slash_validator], unique=True, max_length=100, verbose_name='URL')),
                ('title', models.CharField(max_length=200)),
                ('show_in_navigation', models.BooleanField(default=True, db_index=True)),
                ('content', models.TextField(blank=True)),
                ('template_name', models.CharField(blank=True, max_length=100, choices=[('', 'Default')])),
                ('published', models.BooleanField(default=True, db_index=True)),
                ('login_required', models.BooleanField(editable=False, default=False, db_index=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(null=True, blank=True, to='pages.Page', related_name='children')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
