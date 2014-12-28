__author__ = 'dkoldyaev'

from django.db import models

from simple_pages.models import AbstractModel

from .managers import PageQuerySet

PAGE_PART_TEMPLATES = (
    ('text',        'Text',         ['text_text']),
    # ('galery',      'Galery',       ['galery_photos']),
    # ('image',       'Single Image', ['image_image'])
)

class Page(AbstractModel) :

    objects =           PageQuerySet.as_manager

    name =              models.CharField(blank=False, null=False, max_length=255)
    slug =              models.SlugField(blank=True, null=True)

    meta_title =        models.CharField(blank=True, null=True, max_length=255)
    meta_description =  models.TextField(blank=True, null=True)
    meta_keywords =     models.TextField(blank=True, null=True)

class PageTextPart(AbstractModel) :

    type =              models.CharField(blank=False, null=False, max_length=255, choices=PAGE_PART_TEMPLATES),

    text_text =        models.TextField(blank=True, null=True)

    # galery_header =    models.CharField(blank=True, null=True, max_length=255)
    # galery_photos =    models.ManyToManyField('photo.Photo', blank=True, null=True)