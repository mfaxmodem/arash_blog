from django.contrib import admin
from .models import AIGeneratedContent

@admin.register(AIGeneratedContent)
class AIGeneratedContentAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'created_at')
    search_fields = ('keyword', 'generated_title', 'generated_content')
    readonly_fields = ('created_at',)
