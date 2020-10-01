from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ['title', 'created', 'complete']


admin.site.register(Task, TaskAdmin)
