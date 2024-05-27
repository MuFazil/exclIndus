from django.contrib import admin
from .models import project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'builder', 'project_type', 'project_status', 'size']  # Customize as needed

admin.site.register(project, ProjectAdmin)
