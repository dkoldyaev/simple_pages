from django.shortcuts import render, Http404
from django.template import RequestContext

from .models import Page

# Create your views here.
def page_detail(request, page_slug=None) :

    if not page_slug :
        page_slug = 'index'

    try :   page = Page.objects.get(slug=page_slug)
    except: raise Http404

    return render(
        request,
        'page/page_detail.html',
        {
            'page': page
        },
        context_instance=RequestContext(request)
    )