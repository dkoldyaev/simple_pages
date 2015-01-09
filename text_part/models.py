# -*- coding: utf-8 -*-
__author__ = 'dkoldyaev'

from django.db import models

from simple_pages.models import AbstractModel

TEXT_PART_TEMPLATES = (
    ('oneColText',      u'Текст',               ('oneColText_text',)),
    ('oneColImg',       u'Картинка',            ('oneColImg_img',)),
    ('twoColTextText',  u'Текст + Текст',       ('twoColTextText_textLeft', 'twoColTextText_textRight')),
    ('twoColTextImg',   u'Текст + Картинка',    ('twoColTextImg_textLeft', 'twoColTextImg_imgRight')),
    ('twoColImgText',   u'Картинка + Текст',    ('twoColImgText_imgLeft', 'twoColImgText_textRight')),
    ('twoColImgImg',    u'Картинка + Картинка', ('twoColImgImg_imgLeft', 'twoColImgImg_imgRight')),
)

class TextPart(AbstractModel) :

    order =                         models.PositiveIntegerField(blank=False, null=False, default=0)

    template =                      models.CharField(
        blank=False,
        null=False,
        choices=map(lambda t:t[:2], TEXT_PART_TEMPLATES),
        default='oneColText',
        max_length=255
    )

    oneColText_text =               models.TextField(blank=True, null=True)

    oneColImg_img =                 models.ImageField(blank=True, null=True, upload_to='textPart/oneColImg_img')

    twoColTextText_textLeft =       models.TextField(blank=True, null=True)
    twoColTextText_textRight =      models.TextField(blank=True, null=True)

    twoColTextImg_textLeft =        models.TextField(blank=True, null=True)
    twoColTextImg_imgRight =        models.ImageField(blank=True, null=True, upload_to='textPart/twoColTextImg_imgRight')

    twoColImgText_imgLeft =         models.ImageField(blank=True, null=True, upload_to='textPart/twoColImgText_imgRight')
    twoColImgText_textRight =       models.TextField(blank=True, null=True)

    twoColImgImg_imgLeft =          models.ImageField(blank=True, null=True, upload_to='textPart/twoColImgImg_imgLeft')
    twoColImgImg_imgRight =         models.ImageField(blank=True, null=True, upload_to='textPart/twoColImgImg_imgRight')

    class Meta :

        abstract = True
