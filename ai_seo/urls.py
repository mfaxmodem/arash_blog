from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AIGeneratedContentViewSet

router = DefaultRouter()
router.register('', AIGeneratedContentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]