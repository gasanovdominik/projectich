from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet
from django.urls import path

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='reviews')

urlpatterns = []
urlpatterns += router.urls
