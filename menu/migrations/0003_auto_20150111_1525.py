# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menuitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='target',
            field=models.CharField(default=b'_self', max_length=255, choices=[(b'_self', '\u041a\u0430\u043a \u043e\u0431\u044b\u0447\u043d\u043e'), (b'_blank', '\u0412 \u043d\u043e\u0432\u043e\u0439 \u0432\u043a\u043b\u0430\u0434\u043a\u0435')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
