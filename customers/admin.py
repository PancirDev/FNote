from django.contrib import admin

from .models import Customer, Project, Task


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['company', 'full_name', 'phone']
    search_fields = ['company', 'full_name']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', 'deadline', 'completed']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['task', 'estimate', 'deadline']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
