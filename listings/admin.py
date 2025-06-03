from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'is_active', 'created_at')
    list_filter = ('type', 'is_active', 'location')
    search_fields = ('title', 'description')
