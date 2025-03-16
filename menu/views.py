from rest_framework import viewsets
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MenuItem.objects.filter(parent=None, is_active=True).order_by('order') # type: ignore
    serializer_class = MenuItemSerializer
