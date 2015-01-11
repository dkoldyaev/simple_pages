# -*- coding: utf-8 -*-
__author__ = 'dkoldyaev'

from django.db import models

from simple_pages.models import AbstractModel

MENU_TYPES = [
    ('page',    u'Текстовая страница',   ['page_page',])
]
MENU_TARGETS = [
    ('_self',   u'Как обычно'),
    ('_blank',  u'В новой вкладке'),
]

class MenuItem(AbstractModel):

    text =      models.CharField(blank=False, null=False, max_length=255)
    title =     models.CharField(blank=True, null=False, max_length=255)

    target =    models.CharField(blank=False, null=False, max_length=255, choices=MENU_TARGETS, default=MENU_TARGETS[0][0])

    path =      models.CharField(blank=False, null=True, max_length=255, default='/')

    type =      models.CharField(blank=False, null=False, default='page', choices=map(lambda t:t[:2], MENU_TYPES), max_length=255)

    page_page = models.ForeignKey('page.Page', blank=True, null=True)

    order =     models.PositiveIntegerField(blank=False, null=False, default=0)

    def save(self, *args, **kwargs):

        from django.core.urlresolvers import reverse

        if not self.title :

            self.title = self.text

        if self.type == 'page' :

            if self.page_page.slug == 'index' :
                self.path = reverse('page_detail', kwargs={'page_slug':''})
            else:
                self.path = reverse('page_detail', kwargs={'page_slug':self.page_page.slug})

        super(MenuItem, self).save(*args, **kwargs)