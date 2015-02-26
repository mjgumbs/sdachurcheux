# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blanc_basic_assets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecurringEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField()),
                ('day_of_the_week', models.PositiveSmallIntegerField(db_index=True, choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')])),
                ('time', models.TimeField(db_index=True)),
                ('frequency', models.CharField(max_length=200, blank=True)),
                ('published', models.BooleanField(db_index=True, default=True)),
            ],
            options={
                'ordering': ('day_of_the_week', 'time'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpecialEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('summary', models.CharField(help_text='A short sentence description of the event', max_length=100)),
                ('description', models.TextField(help_text='All of the event details we have')),
                ('start', models.DateTimeField(help_text='Start time/date.', db_index=True)),
                ('start_date', models.DateField(editable=False, db_index=True)),
                ('end', models.DateTimeField(help_text='End time/date.')),
                ('end_date', models.DateField(editable=False, db_index=True)),
                ('published', models.BooleanField(db_index=True, default=True)),
                ('image', blanc_basic_assets.fields.AssetForeignKey(null=True, blank=True, to='assets.Image')),
            ],
            options={
                'ordering': ('start',),
            },
            bases=(models.Model,),
        ),
    ]
