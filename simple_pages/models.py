__author__ = 'dkoldyaev'

from django.db import models

from . import settings
from .managers import AbstractQuerySet

class AbstractModel(models.Model):

    _created =      models.DateTimeField(auto_now_add=True)
    _updated =      models.DateTimeField(auto_now=True)
    _active =       models.BooleanField(blank=False, null=False, default=True)
    _deleted =      models.BooleanField(blank=False, null=False, default=False)
    _comment =      models.TextField(blank=True, null=True)

    public =        models.BooleanField(blank=False, null=False, default=True)

    objects =       AbstractQuerySet.as_manager()

    class Meta:

        abstract =  True
        ordering =  ['id']

    def delete(self, using=None):

        if settings.SAFE_DELETE :
            self._deleted = True

        else :
            super(AbstractModel, self).save(using=using)