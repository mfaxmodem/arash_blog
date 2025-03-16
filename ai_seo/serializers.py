from rest_framework import serializers
from .models import AIGeneratedContent

class AIGeneratedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIGeneratedContent
        fields = '__all__'