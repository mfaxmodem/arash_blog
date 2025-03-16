from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CategoryViewSet, SliderViewSet, TagViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('categories', CategoryViewSet)
router.register('sliders', SliderViewSet)
router.register('tags', TagViewSet)  # Add this line to register the TagViewSet

urlpatterns = [
    path('', include(router.urls)),
]