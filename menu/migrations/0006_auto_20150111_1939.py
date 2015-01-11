# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_menuitem_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='title',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
