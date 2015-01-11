# -*- coding: utf-8 -*-
__author__ = 'dkoldyaev'

from django.contrib import admin

from text_part.admin import TextPartInline
from .models import PageTextPart, Page

class PageTextPartInline(TextPartInline):
    model = PageTextPart

class PageAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,      {'fields':  ['name', 'slug']}),
        ('Meta',    {'fields':  ['meta_title', 'meta_description', 'meta_keywords'],
                     'classes': ['collapse']}),
        ('Admin',   {'fields':  ['_created', '_updated', '_active', '_deleted', '_comment'],
                     'classes': ['collapse']}),
    ]
    readonly_fields = ['_created', '_updated',]
    inlines = [PageTextPartInline,]

admin.site.register(Page, PageAdmin)
