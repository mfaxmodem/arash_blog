from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        (_('اطلاعات اصلی'), {
            'fields': ('title', 'slug', 'content', 'featured_image', 'is_published')
        }),
        (_('سئو'), {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
    )
