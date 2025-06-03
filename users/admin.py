from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Дополнительные поля", {"fields": ("role",)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
