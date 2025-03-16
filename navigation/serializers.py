from rest_framework import serializers
from .models import MenuItem

class RecursiveMenuItemSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class MenuItemSerializer(serializers.ModelSerializer):
    children = RecursiveMenuItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'url', 'order', 'parent', 'children']