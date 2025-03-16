from .models import MenuItem

def menu_items(request):
    """
    Context processor to add menu items to all templates
    """
    main_menu = MenuItem.objects.filter(parent=None, is_active=True).order_by('order')  # type: ignore
    return {
        'main_menu': main_menu
    }