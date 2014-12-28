__author__ = 'dkoldyaev'

from django.db import models

from simple_pages.models import AbstractModel

from .managers import PhotoQuerySet, GaleryQuerySet

class Photo(AbstractModel):

    objects =   PhotoQuerySet.as_manager

    name =      models.CharField(blank=True, null=True, max_length=255)
    image =     models.ImageField(blank=False, null=False, upload_to='photo/photo/image')

class Galery(AbstractModel):

    objects =   GaleryQuerySet.as_manager

    name =      models.CharField(blank=True, null=True, max_length=255)
    description=models.TextField(blank=True, null=True)

    photos =    models.ManyToManyField('photo.Photo', blank=False, null=False)