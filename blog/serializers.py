from rest_framework import serializers
from .models import Category, Tag, Post, Comment, Slider

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', 'description', 'parent', 'order']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'email', 'content', 'parent', 'created_at']
        read_only_fields = ['is_approved']

class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    category_name = serializers.ReadOnlyField(source='category.name', required=False)
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'content', 'excerpt', 'featured_image',
            'categories', 'tags', 'author', 'created_at', 'updated_at',
            'published_at', 'meta_title', 'meta_description', 'meta_keywords',
            'category', 'category_name', 'image'
        ]
        read_only_fields = ['author', 'created_at', 'updated_at']

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'