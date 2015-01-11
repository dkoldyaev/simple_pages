__author__ = 'dkoldyaev'

from django.db import models

from simple_pages.models import AbstractModel
from text_part.models import TextPart

from .managers import PageQuerySet

class Page(AbstractModel) :

    objects =           PageQuerySet.as_manager

    name =              models.CharField(blank=False, null=False, max_length=255)
    slug =              models.SlugField(blank=True, null=True)

    meta_title =        models.CharField(blank=True, null=True, max_length=255)
    meta_description =  models.TextField(blank=True, null=True)
    meta_keywords =     models.TextField(blank=True, null=True)

    @property
    def text_parts(self):

        return PageTextPart.objects.filter(page_id=self.id)

    def save(self, *args, **kwargs):

        if not self.slug or self.slug.strip() == '' :

            from pytils.translit import slugify
            self.slug = slugify(self.name)

        super(Page, self).save(*args, **kwargs)

class PageTextPart(TextPart) :

    page =              models.ForeignKey('page.Page', blank=False, null=False)

    class Meta:

        ordering = ['-order']