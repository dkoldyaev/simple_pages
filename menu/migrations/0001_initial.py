# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20150105_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_updated', models.DateTimeField(auto_now=True)),
                ('_active', models.BooleanField(default=True)),
                ('_deleted', models.BooleanField(default=False)),
                ('_comment', models.TextField(null=True, blank=True)),
                ('public', models.BooleanField(default=True)),
                ('type', models.CharField(default=b'page', max_length=255, choices=[(b'page', '\u0422\u0435\u043a\u0441\u0442\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430')])),
                ('page_page', models.ForeignKey(blank=True, to='page.Page', null=True)),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
