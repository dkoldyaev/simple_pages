# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_updated', models.DateTimeField(auto_now=True)),
                ('_active', models.BooleanField(default=True)),
                ('_deleted', models.BooleanField(default=False)),
                ('_comment', models.TextField(null=True, blank=True)),
                ('public', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('meta_title', models.CharField(max_length=255, null=True, blank=True)),
                ('meta_description', models.TextField(null=True, blank=True)),
                ('meta_keywords', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageTextPart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_updated', models.DateTimeField(auto_now=True)),
                ('_active', models.BooleanField(default=True)),
                ('_deleted', models.BooleanField(default=False)),
                ('_comment', models.TextField(null=True, blank=True)),
                ('public', models.BooleanField(default=True)),
                ('text_text', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
