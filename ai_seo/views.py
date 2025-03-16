from rest_framework import viewsets
from .models import AIGeneratedContent
from .serializers import AIGeneratedContentSerializer

class AIGeneratedContentViewSet(viewsets.ModelViewSet):
    queryset = AIGeneratedContent.objects.all()
    serializer_class = AIGeneratedContentSerializer
