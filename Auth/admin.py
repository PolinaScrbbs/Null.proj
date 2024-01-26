from django.contrib import admin
from .models import CustomUser, Role

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'full_name')
    search_fields = ('username', 'email', 'full_name')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
    



