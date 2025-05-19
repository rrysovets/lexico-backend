from django.contrib import admin
from .models import Module

# Register your models here.


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = "id", "title", "created_at", "updated_at",'is_public','author'
    ordering = "created_at", "updated_at"
    list_display_links = "id", "title"
    list_editable = 'is_public','author'
    
