# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blanc_basic_assets.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ('title',),
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(unique_for_date='date', max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('date_url', models.DateField(db_index=True, editable=False)),
                ('teaser', models.TextField(blank=True)),
                ('content', models.TextField()),
                ('published', models.BooleanField(default=True, db_index=True, help_text='Post will be hidden unless this option is selected')),
                ('category', models.ForeignKey(to='news.Category')),
                ('image', blanc_basic_assets.fields.AssetForeignKey(to='assets.Image', blank=True, null=True)),
            ],
            options={
                'ordering': ('-date',),
                'get_latest_by': 'date',
            },
            bases=(models.Model,),
        ),
    ]
