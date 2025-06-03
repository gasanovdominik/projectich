from rest_framework.routers import DefaultRouter
from .views import SearchQueryViewSet, ViewHistoryViewSet

router = DefaultRouter()
router.register(r'search', SearchQueryViewSet, basename='search')
router.register(r'views', ViewHistoryViewSet, basename='views')

urlpatterns = router.urls
