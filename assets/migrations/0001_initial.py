# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('file', models.FileField(upload_to='assets/file')),
            ],
            options={
                'ordering': ('title',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FileCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ('title',),
                'verbose_name_plural': 'file categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('file', models.ImageField(upload_to='assets/image', width_field='image_width', verbose_name='Image', height_field='image_height')),
                ('image_height', models.PositiveIntegerField(editable=False)),
                ('image_width', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'ordering': ('title',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImageCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ('title',),
                'verbose_name_plural': 'image categories',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ForeignKey(to='assets.ImageCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='file',
            name='category',
            field=models.ForeignKey(to='assets.FileCategory'),
            preserve_default=True,
        ),
    ]
