__author__ = 'dkoldyaev'

from django.db.models.query import QuerySet

from simple_pages.managers import AbstractQuerySet

class PhotoQuerySet(AbstractQuerySet) :

    pass

class GaleryQuerySet(AbstractQuerySet) :

    pass