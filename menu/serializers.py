from rest_framework import serializers
from .models import MenuItem

class RecursiveMenuItemSerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)  # type: ignore
        return serializer.data

class MenuItemSerializer(serializers.ModelSerializer):
    children = RecursiveMenuItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'slug', 'url', 'order', 'children']