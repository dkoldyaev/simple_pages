__author__ = 'dkoldyaev'

def menu_items(request) :

    from .models import MenuItem

    return {
        'menu_items':   MenuItem.objects.all(),
    }