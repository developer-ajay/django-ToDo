from django.contrib import admin

from todo.models import task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task' , 'is_completed','created_at','updated_at')
    search_fields = ('task',)

admin.site.register(task, TaskAdmin)