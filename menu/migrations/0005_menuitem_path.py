# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20150111_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='path',
            field=models.CharField(default=b'/', max_length=255, null=True),
            preserve_default=True,
        ),
    ]
