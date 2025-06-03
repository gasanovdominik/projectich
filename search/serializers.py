from rest_framework import serializers
from .models import SearchQuery, ViewHistory

class SearchQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchQuery
        fields = '__all__'
        read_only_fields = ['user', 'timestamp']

class ViewHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewHistory
        fields = '__all__'
        read_only_fields = ['user', 'viewed_at']
