from .models import MenuItem

def menu_items(request):
    """
    Context processor to add menu items to all templates.
    """
    return {
        'menu_items': MenuItem.objects.filter(parent=None).prefetch_related('children')
    }