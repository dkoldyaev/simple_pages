# -*- coding: utf-8 -*-
__author__ = 'dkoldyaev'

from django.contrib import admin
from suit.admin import SortableTabularInline

from .models import Page, PageTextPart
from text_part.models import TEXT_PART_TEMPLATES

class PageTextPartInline(SortableTabularInline):
    model = PageTextPart
    sortable = 'order'
    fieldsets = [
        (
            t[0],
            {
                'classes':      ['suit-tab', 'suit-tab-{template_name}'.format(template_name=t[0])],
                'fields':       t[2],
            }
        ) for t in TEXT_PART_TEMPLATES
    ]
    suit_form_tabs = [(t[0], t[1]) for t in TEXT_PART_TEMPLATES]
    template = 'admin/edit_inline/tabular_edit_inline_with_tabs.html'

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
