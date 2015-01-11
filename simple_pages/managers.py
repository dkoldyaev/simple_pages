__author__ = 'dkoldyaev'

from django.db.models.query import QuerySet
from django.db.models.manager import Manager

class AbstractQuerySet(QuerySet) :

    def get(self, *args, **kwargs):

        return super(AbstractQuerySet, self.filter(*args, **kwargs)).get()

    def filter(self, *args, **kwargs):

        kwargs['_active'] = kwargs.get('_active', True)
        kwargs['_deleted'] = False

        return super(AbstractQuerySet, self).filter(*args, **kwargs)