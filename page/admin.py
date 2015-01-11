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
        ('template', {'fields':['template']})
    ] + [
        (
            t[0],
            {
                'classes':      ['template-{template_name}'.format(template_name=t[0])],
                'fields':       t[2],
            }
        ) for t in TEXT_PART_TEMPLATES
    ] + [
        ('order', {'fields':['order']})
    ]
    tab_field = 'template'
    suit_form_tabs = [(t[0], t[1]) for t in TEXT_PART_TEMPLATES]
    template = 'admin/edit_inline/tabular_edit_inline_with_tabs.html'
    def get_formset(self, request, obj=None, **kwargs):
        formset = super(PageTextPartInline, self).get_formset(request, obj, **kwargs)
        formset.tab_field = self.tab_field
        formset.sorted_field = self.sortable
        formset.tab_fieldsets = dict(filter(lambda p:p[0] not in [self.sortable, self.tab_field], self.fieldsets))
        return formset
    # def changelist_view(self, request):
    #     return super(PageTextPartInline, self).changelist_view(request, extra_context={
    #         # Put extra fields here and your template will get them in the request.
    #         # Don't accidentally change a variable that the base templates expect.
    #     })

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
