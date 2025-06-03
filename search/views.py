from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count

from .models import SearchQuery, ViewHistory
from .serializers import SearchQuerySerializer, ViewHistorySerializer

class SearchQueryViewSet(viewsets.ModelViewSet):
    queryset = SearchQuery.objects.all().order_by('-timestamp')
    serializer_class = SearchQuerySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def popular(self, request):
        queryset = SearchQuery.objects.values('query').annotate(count=Count('query')).order_by('-count')[:10]
        return Response(queryset)


class ViewHistoryViewSet(viewsets.ModelViewSet):
    queryset = ViewHistory.objects.all().order_by('-viewed_at')
    serializer_class = ViewHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def popular(self, request):
        queryset = ViewHistory.objects.values('listing').annotate(count=Count('listing')).order_by('-count')[:10]
        return Response(queryset)
