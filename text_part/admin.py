__author__ = 'dkoldyaev'

from suit.admin import SortableTabularInline

from .models import TEXT_PART_TEMPLATES

class TextPartInline(SortableTabularInline):
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
        formset = super(TextPartInline, self).get_formset(request, obj, **kwargs)
        formset.tab_field = self.tab_field
        formset.sorted_field = self.sortable
        formset.tab_fieldsets = dict(filter(lambda p:p[0] not in [self.sortable, self.tab_field], self.fieldsets))
        return formset