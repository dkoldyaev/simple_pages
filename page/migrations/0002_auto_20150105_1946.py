# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagetextpart',
            options={'ordering': ['-order']},
        ),
        migrations.RemoveField(
            model_name='pagetextpart',
            name='text_text',
        ),
        migrations.AddField(
            model_name='pagetextpart',
            name='oneColImg_img',
            field=models.ImageField(null=True, upload_to=b'textPart/oneColImg_img', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagetextpart',
            name='oneColText_text',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagetextpart',
            name='order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagetextpart',
            name='page',
            field=models.ForeignKey(default=1, to='page.Page'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagetextpart',
            name='template',
            field=models.CharField(default=b'oneColText', max_length=255, choices=[(b'oneColText', '\u0422\u0435\u043a\u0441\u0442'), (b'oneColImg', '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430'), (b'twoColTextText', '\u0422\u0435\u043a\u0441\u0442 + \u0422\u0435\u043a\u0441\u0442'), (b'twoColTextImg', '\u0422\u0435\u043a\u0441\u0442 + \u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430'), (b'twoColImgText', '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430 + \u0422\u0435\u043a\u0441\u0442'), (b'twoColImgImg', '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430 + \u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagetextpart',
            name='twoColImgImg_imgLeft',
            field=models.ImageField(null=True, upload_to=b'textPart/twoColImgImg_imgLeft', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagetextpart',
            name='twoColImgImg_imgRight',
            field=models.ImageField(null=True, upload_to=b'textPart/twoColImgImg_imgRight', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagetextpart',
            name='twoColImgText_imgLeft',
            field=models.ImageField(null=True, upload_to=b'textPart/twoColImgText_imgRight', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagetextpart',
            name='twoColImgText_textRight',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagetextpart',
            name='twoColTextImg_imgRight',
            field=models.ImageField(null=True, upload_to=b'textPart/twoColTextImg_imgRight', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagetextpart',
            name='twoColTextImg_textLeft',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagetextpart',
            name='twoColTextText_textLeft',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagetextpart',
            name='twoColTextText_textRight',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
