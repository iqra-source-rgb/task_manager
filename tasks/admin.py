from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'priority', 'deadline')  # Fields to display in the admin list view
    list_filter = ('status', 'priority', 'deadline')  # Add filtering options in the admin panel
    search_fields = ('title', 'description')  # Enable search functionality

# Register your models here.
