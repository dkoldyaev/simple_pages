# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20150111_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='name',
            new_name='text',
        ),
    ]
